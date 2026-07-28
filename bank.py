import tkinter as tk
import customtkinter as ctk
import json
import os

# BankSystem 변수
MasterBank = 0


# GUI 변수
bankApp_size = 800

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

    balance_frame = ctk.CTkFrame(
        screen_frame,
        fg_color="transparent"
    )
    balance_frame.pack(pady=(100, 0))

    balance_text = ctk.CTkLabel(
        balance_frame,
        text="현재 잔액",
        font=("맑은 고딕", 20)
    )
    balance_text.pack(pady=(0, 20))

    balance_label = ctk.CTkLabel(
        balance_frame,
        text="0원",
        font=("맑은 고딕", 35, "bold")
    )
    balance_label.pack()

    input_frame = ctk.CTkFrame(
        screen_frame,
        fg_color="transparent"
    )
    input_frame.pack(pady=(35, 10))


    def ClearInputFrame():
        for widget in input_frame.winfo_children():
            widget.destroy()

    def GUIDeposit():
        ClearInputFrame()

        deposit_entry = ctk.CTkEntry(
            input_frame,
            width=300,
            height=45,
            placeholder_text="입금할 금액을 입력하세요",
            font=("맑은 고딕", 16)
        )
        deposit_entry.pack()

        def Deposit():
            global MasterBank

            try:
                amount = int(deposit_entry.get())

                if amount <= 0:
                    message_label.configure(
                        text="0원보다 큰 금액을 입력해 주세요."
                    )
                    return

                MasterBank += amount

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
            input_frame,
            text="입금 확인",
            width=150,
            height=40,
            command=Deposit
        )
        deposit_confirm_button.pack(pady=10)


    def GUIWithdraw():
        ClearInputFrame()

        withdraw_entry = ctk.CTkEntry(
            input_frame,
            width=300,
            height=45,
            placeholder_text="출금할 금액을 입력하세요",
            font=("맑은 고딕", 16)
        )
        withdraw_entry.pack()

        def Withdraw():
            global MasterBank

            try:
                amount = int(withdraw_entry.get())

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
            input_frame,
            text="출금 확인",
            width=150,
            height=40,
            command=Withdraw
        )
        withdraw_confirm_button.pack(pady=10)

    def GUIBalance():
        ClearInputFrame()

        if balance_frame.winfo_manager():
            balance_frame.pack_forget()
        else:
            balance_frame.pack(
                before=input_frame,
                pady=(100, 0)
            )

    button_frame = ctk.CTkFrame(main_frame, width=200)
    button_frame.pack(
        side="right",
        fill="y",
        padx=20,
        pady=20
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
        height=50
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

    message_frame = ctk.CTkFrame(app, height=70)
    message_frame.pack(fill="x", padx=20, pady=20)

    message_label = ctk.CTkLabel(
        message_frame,
        text="원하시는 업무를 선택해 주세요."
    )
    message_label.pack(pady=20)

    app.mainloop()


if __name__ == "__main__":
    StartGUI()