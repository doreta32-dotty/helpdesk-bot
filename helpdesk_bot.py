def helpdesk_bot():
    print("Hello! I'm your IT Helpdesk Bot. Type 'bye' to exit.")
    
    while True:
        problem = input("\nYou: ").lower()
        
        if "bye" in problem or "exit" in problem:
            print("Bot: Goodbye! Ticket closed.")
            break
        elif "wifi" in problem or "internet" in problem:
            print("Bot: 1. Restart router 2. Check if airplane mode is off 3. Forget network & reconnect")
        elif "slow" in problem or "lag" in problem:
            print("Bot: Try: Close unused tabs, Restart laptop, Check Task Manager for high CPU")
        elif "printer" in problem:
            print("Bot: Check: Is printer online? Is cable connected? Restart print spooler service")
        elif "password" in problem or "login" in problem:
            print("Bot: Reset via admin panel or use 'Forgot Password'. Clear cache if stuck.")
        else:
            print("Bot: Logged your issue. An IT tech will contact you. Try describing with keywords like wifi, slow, printer, password.")

helpdesk_bot()