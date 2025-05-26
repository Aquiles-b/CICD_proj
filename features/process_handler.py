import re, pexpect, os


class ProcessHandler:
    def __init__(self, server_ip: str):
        self.result_ptrn = re.compile(r"^=\s(\-?\d+\.\d+)", re.MULTILINE)
        self.command_fail_ptrn = re.compile(r"^=\s(Invalid.*|Division.*)", re.MULTILINE)

        try:
            cur_dir = os.path.dirname(__file__)
            app_rel_path = f"{cur_dir}/../calcApp/calcClient.py"
            self.process = pexpect.spawn(f"python3 {app_rel_path} {server_ip} 9998",
                                         encoding='utf-8', maxread=1)
        except Exception as e:
            raise RuntimeError(f'It was not possible to start the process": {str(e)}')

    def is_connection_successful(self) -> bool:
        self.process.before = ""
        self.process.after = ""

        i = self.process.expect([r"\(Welcome.*", 
                                         pexpect.TIMEOUT,
                                         pexpect.EOF], timeout=2)
        return i == 0

    def the_process_is_alive(self) -> bool:
        if (self.process is not None):
            return self.process.isalive()
        return False

    def run_command(self, exp: str) -> bool:
        if (self.process is None):
            return False

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
        
        if (i == 0):
            self.is_last_command_successful = True
        else:
            self.is_last_command_successful = False

        self.last_result = self.get_result()


        return True

    def get_result(self) -> str:
        if (self.last_process_output is None):
            return ""

        if (not self.is_last_command_successful):
            return ""

        res = self.result_ptrn.findall(self.last_process_output)

        if (not res):
            return ""

        return res[0]
