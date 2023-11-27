import argparse
import cmd
import requests

API_BASE_URL = "http://127.0.0.1:4000"


class MyAPIShell(cmd.Cmd):
    intro = "Welcome to the MyAPI shell. Type help or ? to list commands.\n"
    prompt = "> "

    def do_md5(self, arg):
        """Calculate MD5 hash. Usage: md5 <text>"""
        text = arg.strip()
        self._make_request(f"/md5/{text}")

    def do_factorial(self, arg):
        """Calculate factorial. Usage: factorial <num>"""
        num = arg.strip()
        self._make_request(f"/factorial/{num}")

    def do_fibonacci(self, arg):
        """Generate Fibonacci sequence. Usage: fibonacci <num>"""
        num = arg.strip()
        self._make_request(f"/fibonacci/{num}")

    def do_is_prime(self, arg):
        """Check if a number is prime. Usage: is-prime <num>"""
        num = arg.strip()
        self._make_request(f"/is-prime/{num}")

    def do_slack_alert(self, arg):
        """Send a message to Slack. Usage: slack-alert <message>"""
        message = arg.strip()
        self._make_request(f"/slack-alert/{message}", method="POST")

    def do_keyval_create(self, arg):
        """Create a key-value pair. Usage: keyval-create <storage_key> <storage_val>"""
        args = arg.split()
        if len(args) == 2:
            storage_key, storage_val = args
            self._make_request("/keyval", method="POST", json={"storage-key": storage_key, "storage-val": storage_val})
        else:
            print("Usage: keyval-create <storage_key> <storage_val>")

    def do_keyval_read(self, arg):
        """Read a key-value pair. Usage: keyval-read <storage_key>"""
        storage_key = arg.strip()
        self._make_request(f"/keyval/{storage_key}")

    def do_keyval_update(self, arg):
        """Update a key-value pair. Usage: keyval-update <storage_key> <storage_val>"""
        args = arg.split()
        if len(args) == 2:
            storage_key, storage_val = args
            self._make_request(f"/keyval/{storage_key}", method="PUT", json={"storage-key": storage_key, "storage-val": storage_val})
        else:
            print("Usage: keyval-update <storage_key> <storage_val>")

    def do_keyval_delete(self, arg):
        """Delete a key-value pair. Usage: keyval-delete <storage_key>"""
        storage_key = arg.strip()
        self._make_request(f"/keyval/{storage_key}", method="DELETE")

    def do_exit(self, arg):
        """Exit the shell."""
        print("Exiting the MyAPI shell.")
        return True

    def _make_request(self, endpoint, method="GET", json=None):
        url = f"{API_BASE_URL}{endpoint}"
        response = requests.request(method, url, json=json)
        print(f"Response: {response.status_code}")
        print(response.json() if response.status_code == 200 else response.text)


if __name__ == "__main__":
    MyAPIShell().cmdloop()
