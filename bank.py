import tkinter as tk
import customtkinter as ctk
import json
import os
from datetime import datetime

# BankSystem 변수
MasterBank = 0
TransactionHistory = []
BANK_DATA_FILE = "bank_data.json"

# GUI 변수
bankApp_size = 800


def SaveBankData():
    bank_data = {
        "balance": MasterBank,
        "history": TransactionHistory
    }

    with open(BANK_DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            bank_data,
            file,
            ensure_ascii=False,
            indent=4
        )


def LoadBankData():
    global MasterBank, TransactionHistory

    if not os.path.exists(BANK_DATA_FILE):
        return

    try:
        with open(BANK_DATA_FILE, "r", encoding="utf-8") as file:
            bank_data = json.load(file)

        MasterBank = bank_data.get("balance", 0)
        TransactionHistory = bank_data.get("history", [])

    except (json.JSONDecodeError, OSError):
        MasterBank = 0
        TransactionHistory = []


def StartGUI():
    app = ctk.CTk()

    app.title("BANK SYSTEM")
    app.geometry("800x700")

    title_frame = ctk.CTkFrame(app, height=80)
    title_frame.pack(fill="x", padx=20, pady=20)

    title_label = ctk.CTkLabel(
        title_frame,
        text="은행 계좌 관리 프로그램",
        font=("맑은 고딕", 25, "bold")
    )
    title_label.pack(pady=20)

    main_frame = ctk.CTkFrame(app)
    main_frame.pack(fill="both", expand=True, padx=20)

    screen_frame = ctk.CTkFrame(main_frame, width=500)
    screen_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    button_frame = ctk.CTkFrame(main_frame, width=200)
    button_frame.pack(
        side="right",
        fill="y",
        padx=20,
        pady=20
    )

    message_frame = ctk.CTkFrame(app, height=70)
    message_frame.pack(fill="x", padx=20, pady=20)

    message_label = ctk.CTkLabel(
        message_frame,
        text="원하시는 업무를 선택해 주세요."
    )
    message_label.pack(pady=20)

    current_screen = "balance"

    def ClearScreen():
        for widget in screen_frame.winfo_children():
            widget.destroy()

    def ShowBalance():
        balance_text = ctk.CTkLabel(
            screen_frame,
            text="현재 잔액",
            font=("맑은 고딕", 20)
        )
        balance_text.pack(pady=(100, 20))

        balance_label = ctk.CTkLabel(
            screen_frame,
            text=f"{MasterBank:,}원",
            font=("맑은 고딕", 35, "bold")
        )
        balance_label.pack()

        return balance_label

    def GUIDeposit():
        nonlocal current_screen

        ClearScreen()
        current_screen = "deposit"

        balance_label = ShowBalance()

        deposit_entry = ctk.CTkEntry(
            screen_frame,
            width=300,
            height=45,
            placeholder_text="입금할 금액을 입력하세요",
            font=("맑은 고딕", 16)
        )
        deposit_entry.pack(pady=(35, 10))

        def Deposit():
            global MasterBank, TransactionHistory

            try:
                input_text = deposit_entry.get()

                if len(input_text) > 15:
                    message_label.configure(
                        text="금액은 최대 15자리까지만 입력 가능합니다."
                    )
                    return

                amount = int(input_text)

                if amount <= 0:
                    message_label.configure(
                        text="0원보다 큰 금액을 입력해 주세요."
                    )
                    return

                MasterBank += amount

                now = datetime.now()

                TransactionHistory.append({
                    "type": "입금",
                    "date": now.strftime("%Y-%m-%d"),
                    "time": now.strftime("%H:%M:%S"),
                    "amount": amount,
                    "balance": MasterBank
                })

                SaveBankData()

                balance_label.configure(
                    text=f"{MasterBank:,}원"
                )

                message_label.configure(
                    text=f"{amount:,}원이 입금되었습니다."
                )

                deposit_entry.delete(0, "end")

            except ValueError:
                message_label.configure(
                    text="금액은 숫자로 입력해 주세요."
                )

        deposit_confirm_button = ctk.CTkButton(
            screen_frame,
            text="입금 확인",
            width=150,
            height=40,
            command=Deposit
        )
        deposit_confirm_button.pack(pady=10)

    def GUIWithdraw():
        nonlocal current_screen

        ClearScreen()
        current_screen = "withdraw"

        balance_label = ShowBalance()

        withdraw_entry = ctk.CTkEntry(
            screen_frame,
            width=300,
            height=45,
            placeholder_text="출금할 금액을 입력하세요",
            font=("맑은 고딕", 16)
        )
        withdraw_entry.pack(pady=(35, 10))

        def Withdraw():
            global MasterBank, TransactionHistory

            try:
                input_text = withdraw_entry.get()

                if len(input_text) > 15:
                    message_label.configure(
                        text="금액은 최대 15자리까지만 입력 가능합니다."
                    )
                    return

                amount = int(input_text)

                if amount <= 0:
                    message_label.configure(
                        text="0원보다 큰 금액을 입력해 주세요."
                    )
                    return

                if amount > MasterBank:
                    message_label.configure(
                        text="잔액이 부족합니다."
                    )
                    return

                MasterBank -= amount

                now = datetime.now()

                TransactionHistory.append({
                    "type": "출금",
                    "date": now.strftime("%Y-%m-%d"),
                    "time": now.strftime("%H:%M:%S"),
                    "amount": amount,
                    "balance": MasterBank
                })

                SaveBankData()

                balance_label.configure(
                    text=f"{MasterBank:,}원"
                )

                message_label.configure(
                    text=f"{amount:,}원이 출금되었습니다."
                )

                withdraw_entry.delete(0, "end")

            except ValueError:
                message_label.configure(
                    text="금액은 숫자로 입력해 주세요."
                )

        withdraw_confirm_button = ctk.CTkButton(
            screen_frame,
            text="출금 확인",
            width=150,
            height=40,
            command=Withdraw
        )
        withdraw_confirm_button.pack(pady=10)

    def GUIBalance():
        nonlocal current_screen

        if current_screen == "balance":
            ClearScreen()
            current_screen = "empty"

            message_label.configure(
                text="잔액 조회 화면을 닫았습니다."
            )

        else:
            ClearScreen()
            ShowBalance()

            current_screen = "balance"

            message_label.configure(
                text=f"현재 잔액은 {MasterBank:,}원입니다."
            )

    def GUIHistory():
        nonlocal current_screen

        ClearScreen()
        current_screen = "history"

        history_frame = ctk.CTkScrollableFrame(
            screen_frame,
            label_text="거래 내역"
        )
        history_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        if len(TransactionHistory) == 0:
            empty_label = ctk.CTkLabel(
                history_frame,
                text="거래 내역이 없습니다.",
                font=("맑은 고딕", 16)
            )
            empty_label.pack(pady=30)

            message_label.configure(
                text="저장된 거래 내역이 없습니다."
            )
            return

        for transaction in reversed(TransactionHistory):
            history_item = ctk.CTkFrame(history_frame)
            history_item.pack(
                fill="x",
                padx=10,
                pady=5
            )

            if transaction["type"] == "입금":
                amount_text = f'+{transaction["amount"]:,}원'
            else:
                amount_text = f'-{transaction["amount"]:,}원'

            history_label = ctk.CTkLabel(
                history_item,
                text=(
                    f'{transaction["type"]}  |  '
                    f'{transaction["date"]} {transaction["time"]}  |  '
                    f'{amount_text}  |  '
                    f'잔액 {transaction["balance"]:,}원'
                ),
                font=("맑은 고딕", 11)
            )
            history_label.pack(
                fill="x",
                padx=10,
                pady=12
            )

        message_label.configure(
            text=f"총 {len(TransactionHistory)}개의 거래 내역입니다."
        )

    deposit_button = ctk.CTkButton(
        button_frame,
        text="입금",
        width=150,
        height=50,
        command=GUIDeposit
    )
    deposit_button.pack(padx=20, pady=10)

    withdraw_button = ctk.CTkButton(
        button_frame,
        text="출금",
        width=150,
        height=50,
        command=GUIWithdraw
    )
    withdraw_button.pack(padx=20, pady=10)

    balance_button = ctk.CTkButton(
        button_frame,
        text="잔액 조회",
        width=150,
        height=50,
        command=GUIBalance
    )
    balance_button.pack(padx=20, pady=10)

    history_button = ctk.CTkButton(
        button_frame,
        text="거래 내역",
        width=150,
        height=50,
        command=GUIHistory
    )
    history_button.pack(padx=20, pady=10)

    exit_button = ctk.CTkButton(
        button_frame,
        text="종료",
        width=150,
        height=50,
        command=app.destroy
    )
    exit_button.pack(padx=20, pady=10)

    ShowBalance()

    app.mainloop()


if __name__ == "__main__":
    LoadBankData()
    StartGUI()