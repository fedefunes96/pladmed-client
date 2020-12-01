from config.operations.traceroute import TRACEROUTE_PARAMS, GENERAL_PARAMS, DNS_PARAMS


class ParamsParser:
    def parse_params(self, params, valid_params):
        command = ""

        for cmd in params:
            if cmd in valid_params:
                manager = valid_params[cmd]

                manager.validate(params[cmd])

                command += manager.parse_command(params[cmd]) + " "

        return command.rstrip()

    def parse_traceroute(self, params):
        general_cmd = self.parse_params(params, GENERAL_PARAMS).split(' ')
        sub_cmd = ["trace " + self.parse_params(params, TRACEROUTE_PARAMS)]

        return sub_cmd + general_cmd

    def parse_dns(self, params):
        return [self.parse_params(params, DNS_PARAMS)]
