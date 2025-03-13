from robot.api.deco import library, keyword
from robot.api.exceptions import Failure, FatalError, ContinuableFailure
from robot.api import logger

import pexpect, re, os


@library(scope="GLOBAL")
class ProcessHandler:
    def __init__(self):
        self.process = None
        self.result_ptrn = re.compile(r"^=\s(\-?\d+\.\d+)", re.MULTILINE)
        self.command_fail_ptrn = re.compile(r"^=\s(Invalid.*|Division.*)", re.MULTILINE)

    @keyword
    def the_process_has_started_with(self, *args) -> None:
        try:
            if (self.process is not None):
                self.process.close()
            cur_dir = os.path.dirname(__file__)
            app_rel_path = f"{cur_dir}/../../calcApp/calcClient.py"
            cli_args = " ".join(args)
            self.process = pexpect.spawn(f"python3 {app_rel_path} {cli_args}", encoding='utf-8',
                                         maxread=1)
        except Exception as e:
            raise FatalError(f'It was not possible to start the process": {str(e)}')

    @keyword
    def the_welcome_message_appeared(self) -> None:
        if (self.process is None):
            raise Failure("No process started!")
        self.process.before = ""
        self.process.after = ""

        i = self.process.expect([r"\(Welcome.*", 
                                         pexpect.TIMEOUT,
                                         pexpect.EOF], timeout=3)
        logger.debug(f"{i}: {self.process.before}")
        logger.debug(str(self.process.after))
        if (i != 0):
            raise Failure("Welcome message has not appeared!")

    @keyword
    def the_process_must_be_terminated(self) -> None:
        if (self.process is not None):
            if (self.process.isalive()):
                raise Failure("Process still running!")

    @keyword
    def the_expression_provided_is(self, exp: str) -> None:
        if (self.process is None):
            raise Failure("No process started!")

        try:
            self.process.read_nonblocking(size=4096, timeout=0)
        except:
            pass

        self.process.before = ""
        self.process.after = ""
        self.process.sendline(exp)

        i = self.process.expect([self.result_ptrn, 
                                 self.command_fail_ptrn,
                                 pexpect.TIMEOUT, pexpect.EOF], timeout=1)

        self.last_process_output = str(self.process.before) + str(self.process.after)
        logger.debug(f"index: {i}")
        logger.debug(f"{self.last_process_output}")

        if (i == 0):
            self.is_last_command_successful = True
        else:
            self.is_last_command_successful = False

        self.last_result = self.get_result()
        logger.debug(f"Result: {self.last_result}")

    @keyword
    def the_command_must_be_successful(self) -> None:
        if (not self.is_last_command_successful):
            raise ContinuableFailure("The last command failed!!")

    @keyword
    def the_command_must_be_unsuccessful(self) -> None:
        if (self.is_last_command_successful):
            raise ContinuableFailure("The last command was successful!!")

    @keyword
    def the_result_should_be_equals_to(self, test_res: str) -> None:
        if (self.last_result != test_res):
            raise ContinuableFailure(f"Result {self.last_result} is not equals to {test_res}!!")

    @keyword
    def the_result_should_not_be_equals_to(self, test_res: str) -> None:
        if (self.last_result == test_res):
            raise ContinuableFailure(f"Result {self.last_result} is equals to {test_res}!!")

    def get_result(self) -> str:
        if (self.last_process_output is None):
            return ""

        if (not self.is_last_command_successful):
            return ""

        res = self.result_ptrn.findall(self.last_process_output)

        if (not res):
            return ""

        return res[0]

