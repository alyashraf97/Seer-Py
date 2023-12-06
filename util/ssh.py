import paramiko


class SSHSessionFactory:
    def __init__(self, username, password=None, key_filename=None, key_type=None):
        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.key_type = key_type

    def create(self, hostname):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if self.password:
            ssh.connect(hostname, username=self.username, password=self.password)
        elif self.key_filename:
            private_key = self._get_private_key()
            ssh.connect(hostname, username=self.username, pkey=private_key)
        else:
            raise ValueError("Either password or key_filename must be provided.")
        return ssh

    def _get_private_key(self):
        with open(self.key_filename, 'r') as key_file:
            first_word = key_file.readline().split()[0]
        key_types = {
            'rsa': paramiko.RSAKey,
            'dss': paramiko.DSSKey,
            'ecdsa': paramiko.ECDSAKey,
            'ed25519': paramiko.Ed25519Key
        }
        key_type = self.key_type.lower() if self.key_type else first_word
        if key_type not in key_types:
            raise ValueError("Unsupported key type. Supported types are: rsa, dss, ecdsa, ed25519")
        return key_types[key_type].from_private_key_file(self.key_filename)


class SSHManager:
    def __init__(self, ssh_factory, filename):
        self.filename = filename
        self.ssh_factory = ssh_factory
        self.hostnames = self.read_hostnames_from_file(filename)

    def create_ssh_sessions(self):
        sessions = {hostname: self.ssh_factory.create(hostname) for hostname in self.hostnames}
        return sessions

    @staticmethod
    def read_hostnames_from_file(filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file]


class SSHExecutor:
    def __init__(self, ssh_sessions):
        self.ssh_sessions = ssh_sessions

    def execute_command(self, command):
        results = {}
        for hostname, session in self.ssh_sessions.items():
            stdin, stdout, stderr = session.exec_command(command)
            results[hostname] = stdout.read().decode('utf-8')
        return results

    def execute_bulk(self, commands):
        results = {}
        for command in commands:
            results[command] = self.execute_command(command)
        return results
