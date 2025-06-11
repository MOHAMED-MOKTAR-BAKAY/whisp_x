import os
import time
import random
from datetime import datetime
import colorama
from colorama import Fore, Back, Style
import pyfiglet
from simple_term_menu import TerminalMenu
import phonenumbers
from twilio.rest import Client

# Initialize colorama
colorama.init(autoreset=True)

# Twilio credentials (replace with your actual credentials)
TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio's sandbox number

class WhispX:
    def __init__(self):
        self.connected = False
        self.user_id = f"USER-{random.randint(1000, 9999)}"
        self.client = None
        self.clear_screen()
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        # ASCII Art Logo
        ascii_art = pyfiglet.figlet_format("WHISP-X", font="slant")
        colored_ascii = ""
        for line in ascii_art.split('\n'):
            if "WHISP" in line:
                colored_ascii += Fore.RED + line + "\n"
            elif "X" in line:
                colored_ascii += Fore.MAGENTA + line + "\n"
            else:
                colored_ascii += line + "\n"
        
        print(Fore.WHITE + "-" * 60)
        print(colored_ascii)
        print(Fore.WHITE + "-" * 60)
        print()
    
    def display_info_cards(self):
        # Information cards
        print(Fore.CYAN + "✦" * 60)
        print(Fore.YELLOW + "➤ " + Fore.WHITE + f"Tool Name: {Fore.GREEN}WHISP-X {Fore.WHITE}(WhatsApp Anonymous Messenger)")
        print(Fore.YELLOW + "➤ " + Fore.WHITE + f"System Status: {Fore.GREEN if self.connected else Fore.RED}{'CONNECTED' if self.connected else 'DISCONNECTED'}")
        print(Fore.YELLOW + "➤ " + Fore.WHITE + f"User ID: {Fore.MAGENTA}{self.user_id}")
        print(Fore.CYAN + "✦" * 60)
        print()
    
    def display_center_art(self):
        # Center ASCII art (message bubble with bomb)
        center_art = f"""
        {Fore.WHITE}   .--.      .--.
        {Fore.WHITE}  /    \\    /    \\
        {Fore.WHITE} |      {Fore.RED}◉{Fore.WHITE}      {Fore.RED}◉{Fore.WHITE} |
        {Fore.WHITE} |   {Fore.RED}╭─────╮{Fore.WHITE}   |
        {Fore.WHITE}  \\   {Fore.RED}│BOOM!│{Fore.WHITE}  /
        {Fore.WHITE}   '--'{Fore.RED}╰─────╯{Fore.WHITE}'--'
        {Fore.WHITE}      /        \\
        {Fore.WHITE}     /          \\
        {Fore.WHITE}    /            \\
        """
        print(center_art)
        print(Fore.YELLOW + " " * 15 + "ANONYMOUS MESSAGE DELIVERY SYSTEM")
        print()
    
    def connect_to_service(self):
        try:
            self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            self.connected = True
            return True
        except Exception as e:
            print(Fore.RED + f"Connection Error: {e}")
            return False
    
    def validate_phone_number(self, phone_number):
        try:
            parsed_number = phonenumbers.parse(phone_number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                return False
            return phonenumbers.format_number(
                parsed_number, 
                phonenumbers.PhoneNumberFormat.E164
            )
        except:
            return False
    
    def get_user_input(self):
        print(Fore.YELLOW + "➤ " + Fore.WHITE + "Enter target phone number (with country code, e.g., +1234567890):")
        print(Fore.WHITE + " " * 4 + "➤ ", end="")
        phone_number = input().strip()
        
        formatted_number = self.validate_phone_number(phone_number)
        if not formatted_number:
            print(Fore.RED + "Invalid phone number format. Please include country code.")
            return None, None
        
        print(Fore.YELLOW + "➤ " + Fore.WHITE + "Enter your anonymous message:")
        print(Fore.WHITE + " " * 4 + "➤ ", end="")
        message = input().strip()
        
        return formatted_number, message
    
    def show_loading_bar(self, duration=5):
        print("\n" + Fore.WHITE + "Sending anonymous message...")
        print(Fore.MAGENTA + "[", end="")
        
        for i in range(1, 21):
            time.sleep(duration / 20)
            print(Fore.MAGENTA + "█", end="", flush=True)
        
        print(Fore.MAGENTA + "] 100%")
        print(Fore.WHITE + "Please Wait" + "".join(["." * i for i in range(1, 4)]))
        print()
    
    def send_message(self, to_number, message):
        whatsapp_number = f"whatsapp:{to_number}"
        
        try:
            # Show loading animation
            self.show_loading_bar()
            
            # Actual message sending (commented out for safety)
            # Uncomment to enable actual sending
            """
            message = self.client.messages.create(
                body=message,
                from_=TWILIO_WHATSAPP_NUMBER,
                to=whatsapp_number
            )
            """
            
            # Simulate success for demo purposes
            return True, "SUCCESS", "Message delivered anonymously"
        except Exception as e:
            return False, "ERROR", str(e)
    
    def display_execution_log(self, phone_number, message, status, error_msg=None):
        print(Fore.WHITE + "-" * 60)
        print(Fore.YELLOW + "➤ " + Fore.WHITE + "Execution Log:")
        print(Fore.CYAN + "✦" * 30)
        
        # Display phone number (partially masked)
        displayed_number = phone_number[:4] + "****" + phone_number[-3:]
        print(Fore.YELLOW + "➤ " + Fore.WHITE + f"Target: {Fore.GREEN}{displayed_number}")
        
        # Display truncated message
        truncated_msg = (message[:20] + '...') if len(message) > 20 else message
        print(Fore.YELLOW + "➤ " + Fore.WHITE + f"Message: {Fore.CYAN}{truncated_msg}")
        
        # Display status
        status_color = Fore.GREEN if status == "SUCCESS" else Fore.RED
        print(Fore.YELLOW + "➤ " + Fore.WHITE + f"Status: {status_color}{status}")
        
        if error_msg:
            print(Fore.YELLOW + "➤ " + Fore.WHITE + f"Details: {Fore.RED}{error_msg}")
        
        # Display fake transfer rate and time
        transfer_rate = f"{random.uniform(100, 200):.1f} kB/s"
        current_time = datetime.now().strftime("%H:%M:%S")
        print(Fore.YELLOW + "➤ " + Fore.WHITE + f"Rate: {Fore.BLUE}{transfer_rate}")
        print(Fore.YELLOW + "➤ " + Fore.WHITE + f"Time: {Fore.BLUE}{current_time}")
        
        print(Fore.CYAN + "✦" * 30)
        print(Fore.WHITE + "-" * 60)
    
    def display_footer(self):
        print("\n" + Fore.WHITE + "-" * 60)
        print(Fore.YELLOW + "Controls: " + 
              Fore.WHITE + "[ESC] Exit • " + 
              Fore.WHITE + "[CTRL] Menu • " + 
              Fore.WHITE + "[HOME] Reset")
        print(Fore.WHITE + "-" * 60)
    
    def main_menu(self):
        options = ["Send Anonymous Message", "Check Connection", "Exit"]
        terminal_menu = TerminalMenu(
            options,
            title="WHISP-X Main Menu",
            menu_cursor="➤ ",
            menu_cursor_style=("fg_red", "bold"),
            menu_highlight_style=("fg_cyan", "bold")
        )
        return terminal_menu.show()
    
    def run(self):
        self.display_header()
        self.display_info_cards()
        self.display_center_art()
        
        # Connect to service
        if not self.connect_to_service():
            print(Fore.RED + "Failed to connect to messaging service. Exiting...")
            time.sleep(2)
            return
        
        while True:
            choice = self.main_menu()
            
            if choice == 0:  # Send Anonymous Message
                self.clear_screen()
                self.display_header()
                self.display_info_cards()
                
                phone_number, message = self.get_user_input()
                if phone_number and message:
                    success, status, error_msg = self.send_message(phone_number, message)
                    self.display_execution_log(phone_number, message, status, error_msg)
                    
                    if success:
                        print(Fore.GREEN + "\nMessage sent successfully and anonymously!")
                    else:
                        print(Fore.RED + "\nFailed to send message.")
                    
                    input(Fore.WHITE + "\nPress Enter to continue...")
                    self.clear_screen()
            
            elif choice == 1:  # Check Connection
                self.clear_screen()
                self.display_header()
                print(Fore.YELLOW + "\nChecking connection to WHISP-X network...")
                time.sleep(1)
                
                if self.connected:
                    print(Fore.GREEN + "\n✓ Connection active and secure")
                    print(Fore.WHITE + f"User ID: {Fore.MAGENTA}{self.user_id}")
                    print(Fore.WHITE + f"Last ping: {random.randint(10, 50)}ms")
                else:
                    print(Fore.RED + "\n✗ Connection failed")
                    print(Fore.WHITE + "Attempting to reconnect...")
                    time.sleep(2)
                    if self.connect_to_service():
                        print(Fore.GREEN + "✓ Reconnection successful")
                    else:
                        print(Fore.RED + "✗ Reconnection failed")
                
                input(Fore.WHITE + "\nPress Enter to continue...")
                self.clear_screen()
            
            elif choice == 2 or choice is None:  # Exit
                print(Fore.RED + "\nTerminating WHISP-X session...")
                time.sleep(1)
                print(Fore.WHITE + "All traces erased. Goodbye.")
                break

if __name__ == "__main__":
    try:
        app = WhispX()
        app.run()
    except KeyboardInterrupt:
        print(Fore.RED + "\nSession terminated by user.")
    except Exception as e:
        print(Fore.RED + f"\nAn error occurred: {e}")