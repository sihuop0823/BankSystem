import tkinter as tk
import customtkinter as ctk

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

    balance_text = ctk.CTkLabel(
        screen_frame,
        text="현재 잔액",
        font=("맑은 고딕", 20)
    )
    balance_text.pack(pady=(100, 20))

    balance_label = ctk.CTkLabel(
        screen_frame,
        text="0원",
        font=("맑은 고딕", 35, "bold")
    )
    balance_label.pack()

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
        height=50
    )
    deposit_button.pack(padx=20, pady=10)

    withdraw_button = ctk.CTkButton(
        button_frame,
        text="출금",
        width=150,
        height=50
    )
    withdraw_button.pack(padx=20, pady=10)

    balance_button = ctk.CTkButton(
        button_frame,
        text="잔액 조회",
        width=150,
        height=50
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