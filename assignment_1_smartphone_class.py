# Assignment 1🏗️
# Simple Smartphone class 

class Smartphone:
    """A simple smartphone class"""
    
    def __init__(self, brand, model, color):
        # Basic attributes (properties)
        self.brand = brand
        self.model = model
        self.color = color
        self.is_on = False
        self.battery = 100
    
    def turn_on(self):
        """Turn on the phone"""
        self.is_on = True
        print(f"📱 {self.model} is now ON!")
    
    def turn_off(self):
        """Turn off the phone"""
        self.is_on = False
        print(f"📱 {self.model} is now OFF!")
    
    def make_call(self, number):
        """Make a phone call"""
        if self.is_on:
            print(f"📞 Calling {number} from {self.model}...")
        else:
            print(f"❌ Phone is off! Turn on {self.model} first!")
    
    def send_message(self, message):
        """Send a text message"""
        if self.is_on:
            print(f"💬 Sending: '{message}' from {self.model}")
        else:
            print(f"❌ Phone is off! Turn on {self.model} first!")
    
    def __str__(self):
        """Show phone info when we print it"""
        return f"{self.brand} {self.model} ({self.color})"


# Inheritance: Child classes inherit from parent class
class AndroidPhone(Smartphone):
    """Android phone - gets everything from Smartphone + extra features"""
    
    def download_app(self, app_name):
        """Download app from Google Play Store"""
        if self.is_on:
            print(f"📱 Downloading {app_name} from Google Play Store")
        else:
            print(f"❌ Phone is off! Turn on {self.model} first!")


class iPhone(Smartphone):
    """iPhone - gets everything from Smartphone + extra features"""
    
    def download_app(self, app_name):
        """Download app from App Store"""
        if self.is_on:
            print(f"📱 Downloading {app_name} from App Store")
        else:
            print(f"❌ Phone is off! Turn on {self.model} first!")


# Test our classes
def main():
    print("🏗️ Creating Smartphones")
    print("=" * 30)
    
    # Create objects (instances) of our classes
    my_android = AndroidPhone("Samsung", "Galaxy A54", "Blue")
    my_iphone = iPhone("Apple", "iPhone 13", "Red")
    
    # Show our phones
    print(f"📱 Phone 1: {my_android}")
    print(f"📱 Phone 2: {my_iphone}")
    
    print("\n🔌 Turning on phones:")
    my_android.turn_on()
    my_iphone.turn_on()
    
    print("\n📞 Making calls:")
    my_android.make_call("123-456-7890")
    my_iphone.make_call("987-654-3210")
    
    print("\n💬 Sending messages:")
    my_android.send_message("Hello from Android!")
    my_iphone.send_message("Hello from iPhone!")
    
    print("\n📱 Downloading apps:")
    my_android.download_app("Instagram")  # Uses Google Play Store
    my_iphone.download_app("Instagram")   # Uses App Store
    
    print("\n🔌 Turning off phones:")
    my_android.turn_off()
    my_iphone.turn_off()
    
    print("\n✅ Done!")


# Run the program
if __name__ == "__main__":
    main()
