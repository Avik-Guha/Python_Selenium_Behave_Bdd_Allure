import subprocess


if __name__ == '__main__':

    # command = f'behave Features/Registration1.feature -D environment=QA -D browser=Chrome -f allure -o .\Reports'
    command = f'behave Features/Registration1.feature -D environment=QA -D browser=Chrome -f allure -o .\Reports'

    rs = subprocess.run(command, shell=True)

