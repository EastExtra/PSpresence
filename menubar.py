import time
import rumps
from presence import get_active_app, get_active_window_title, connect
from par import parse_title


class PresenceApp(rumps.App):
    def __init__(self):
        super().__init__("PS", icon="images/small-logo.png", template=True, quit_button=None)  

        self.rpc = None
        self.last_state = None
        self.paused = False
        self.start_time = time.time()

        self.status_item = rumps.MenuItem("Starting...")
        self.pause_item = rumps.MenuItem("Pause sharing", callback=self.toggle_pause)
        self.about_item = rumps.MenuItem("About PSpresence", callback=self.show_about)
        self.quit_item = rumps.MenuItem("Quit", callback=self.quit_app)
        self.menu = [self.status_item, self.pause_item, self.about_item, self.quit_item]
       
        self.timer = rumps.Timer(self.tick, 2)
        self.timer.start()

    def tick(self, _):
        if self.paused:
            return

        app = get_active_app()
        title = get_active_window_title()
        current_state = (app, title)

        if self.rpc is None:
            try:
                self.rpc = connect()
            except Exception:
                self.status_item.title = "Waiting for Discord..."
                return  # no sleep here, we'd freeze the menu; the timer retries in 2s

        if current_state != self.last_state:
            try:
                parsed = parse_title(app, title)
                self.rpc.update(
                    details=parsed["details"],
                    state=parsed["state"],
                    start=self.start_time,
                )
                self.status_item.title = f"{parsed['details']} | {parsed['state']}"
                self.last_state = current_state
            except Exception:
                self.rpc = None
                self.last_state = None
                self.status_item.title = "Reconnecting to Discord..."

    def toggle_pause(self, sender):
        self.paused = not self.paused
        if self.paused:
            sender.title = "Resume sharing"
            self.title = "⏸"
            self.status_item.title = "Paused (nothing shared)"
            self.clear_presence()
        else:
            sender.title = "Pause sharing"
            self.title =  None
            self.last_state = None  

    def clear_presence(self):
        if self.rpc is not None:
            try:
                self.rpc.clear()
            except Exception:
                self.rpc = None
        self.last_state = None
    
    def show_about(self, _): 
        rumps.alert(
            title="PSpresence",
            message="Shows what you're working on as a Discord status.\n\nVersion 0.1 (early WIP)",
            ok="Close",
            icon_path="images/logo.png",
        )

    def quit_app(self, _):
        self.clear_presence()
        rumps.quit_application()


if __name__ == "__main__":
    PresenceApp().run()