import sys

class ATM:
    atm_pin: int = 8184

    def __init__(self, pin: int) -> None:
        self.pin = pin
        self.amount = 0

    def check_pin(self, pin) -> bool:
        return pin == self.atm_pin

    def balance(self) -> int:
        return self.amount

    def deposit(self, amount: int) -> str:
        self.amount += amount
        return f"Total amount is {self.amount}"

    def withdraw(self, amount: int) -> str:
        if amount > self.amount:
            return "Insufficient balance"
        self.amount -= amount
        return f"Total amount is {self.amount}"


if __name__ == "__main__":


    get_pin = input("Enter your ATM PIN: ")
    if not get_pin.isdigit():
        print("PIN must be numeric.")
        sys.exit()
    mano_atm = ATM(int(get_pin))


    if not mano_atm.check_pin(int(get_pin)):
        print("Invalid PIN.")
        sys.exit()
    print("Welcome to Mano ATM")
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        choice = input("Choose an option (1/2/3): ")

        if not choice.isdigit():
            print("Choice must be numeric.")
            break

        match int(choice):
            case 1:
                deposit_amount = input("Enter amount to deposit: ")
                if not deposit_amount.isdigit():
                    print("Amount must be numeric.")
                    break
                print(mano_atm.deposit(int(deposit_amount)))
            case 2:
                withdraw_amount = input("Enter amount to withdraw: ")
                if not withdraw_amount.isdigit():
                    print("Amount must be numeric.")
                    break
                print(mano_atm.withdraw(int(withdraw_amount)))
            case 3:
                print(f"Total amount is {mano_atm.balance()}")
            case _:
                print("Invalid choice.")
