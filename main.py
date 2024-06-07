from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp, sp


import os
from datetime import datetime

class GetStartedScreen(Screen):
    def __init__(self, **kwargs):
        super(GetStartedScreen, self).__init__(**kwargs)
        with self.canvas.before:
            self.rect = Rectangle(source='assets/background.png', size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        layout = FloatLayout()
        self.button = Button(
            background_normal='assets/get_started_button.png',
            background_down='assets/get_started_button_pressed.png',
            size_hint=(0.65, 0.11),
            pos_hint={'center_x': 0.5, 'y': 0.1}
        )
        self.button.bind(on_press=self.on_button_press)
        layout.add_widget(self.button)
        self.add_widget(layout)
    
    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def on_button_press(self, instance):
        anim = Animation(size_hint=(0.7, 0.15), duration=0.2)
        anim.start(self.button)
        anim.bind(on_complete=self.switch_to_onboarding)

    def switch_to_onboarding(self, *args):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = 'screen1'

class OnboardingScreen(Screen):
    def __init__(self, bg_image, **kwargs):
        super(OnboardingScreen, self).__init__(**kwargs)
        with self.canvas.before:
            self.rect = Rectangle(source=bg_image, size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        layout = FloatLayout()
        self.button = Button(
            background_normal='assets/continue_button.png',
            background_down='assets/continue_button_pressed.png',
            size_hint=(0.7, 0.12),
            pos_hint={'center_x': 0.5, 'y': 0.05}
        )
        self.button.bind(on_press=self.on_button_press)
        layout.add_widget(self.button)
        self.add_widget(layout)
    
    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def on_button_press(self, instance):
        app = App.get_running_app()
        screen_manager = app.root
        next_screen_number = int(self.name[-1]) + 1
        next_screen_name = f'screen{next_screen_number}' if next_screen_number <= 4 else 'home'
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = next_screen_name

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        with self.canvas.before:
            self.rect = Rectangle(source='assets/home_screen.png', size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        layout = FloatLayout()
        
        # Button for navigating to journal entry screen
        self.add_button = Button(
            background_normal='assets/add_button.png',
            background_down='assets/add_button.png',
            size_hint=(0.25, 0.16),
            pos_hint={'center_x': 0.5, 'y': 0.03}
        )
        self.add_button.bind(on_press=self.on_add_button_press)
        layout.add_widget(self.add_button)

        # Button for navigating to saved journals screen
        self.saved_journals_button = Button(
            background_normal='assets/saved_journals_button.png',
            background_down='assets/saved_journals_button.png',
            size_hint=(0.8, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.8}
        )
        self.saved_journals_button.bind(on_press=self.on_saved_journals_button_press)
        layout.add_widget(self.saved_journals_button)
        
       

                # Button for navigating to about developer screen
        self.about_button = Button(
            background_normal='assets/about_button.png',  # Use your button image here
            background_down='assets/about_button.png',  # If you have a pressed state image
            size_hint=(0.18, 0.09),
            pos_hint={'center_x': 0.91, 'y': 0.91}
        )
        self.about_button.bind(on_press=self.on_about_button_press)
        layout.add_widget(self.about_button)
        
        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def on_add_button_press(self, instance):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = 'journal'

    def on_saved_journals_button_press(self, instance):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = 'saved_journals'

    def on_about_button_press(self, instance):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = 'about_developer'


class ImageWidget(FloatLayout):
    def clear_images(self):
        for widget in self.children[:]:
            if isinstance(widget, Image):
                self.remove_widget(widget)

from kivy.uix.screenmanager import SlideTransition

class AboutDeveloperScreen(Screen):
    def __init__(self, **kwargs):
        super(AboutDeveloperScreen, self).__init__(**kwargs)
        
        layout = FloatLayout()
        
        # Set the background image
        self.background = Image(source='assets/about_background.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.background)
        
        # Add a back button with custom image
        self.back_button = Button(
            background_normal='assets/back_button.png',
            background_down='assets/back_button_pressed.png',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.8, 'y': 0.08}
        )
        self.back_button.bind(on_press=self.on_back_button_press)
        layout.add_widget(self.back_button)
        
        self.add_widget(layout)

    def on_back_button_press(self, instance):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='right')
        screen_manager.current = 'home'


class JournalScreen(Screen):
    def __init__(self, **kwargs):
        super(JournalScreen, self).__init__(**kwargs)
        with self.canvas.before:
            self.rect = Rectangle(source='assets/journal_background.png', size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        layout = FloatLayout()
        
        # Add a TextInput for typing
        self.text_input = TextInput(
            hint_text='Start typing your journal...',
            size_hint=(0.8, 0.4),
            pos_hint={'center_x': 0.5, 'top': 0.8},
            multiline=True
        )
        layout.add_widget(self.text_input)
        
        # Add the DoodleWidget
        self.doodle_widget = DoodleWidget(size_hint=(0.8, 0.4), pos_hint={'center_x': 0.5, 'top': 0.8})
        self.doodle_widget.opacity = 0  # Initially hidden
        layout.add_widget(self.doodle_widget)

        # Toggle button to switch between text input and doodling
        self.toggle_button = Button(
            background_normal='assets/switch_to_doodle_button.png',
            background_down='assets/switch_to_doodle_button_pressed.png',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.3, 'y': 0.02}
        )
        self.toggle_button.bind(on_press=self.toggle_input_mode)
        layout.add_widget(self.toggle_button)



        # Add a save button with custom image
        self.save_button = Button(
            background_normal='assets/save_button.png',
            background_down='assets/save_button_pressed.png',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.1, 'y': 0.02}
        )
        self.save_button.bind(on_press=self.on_save_button_press)
        layout.add_widget(self.save_button)
        
        # Add a clear button with custom image
        self.clear_button = Button(
            background_normal='assets/clear_button.png',
            background_down='assets/clear_button_pressed.png',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.7, 'y': 0.02}
        )
        self.clear_button.bind(on_press=self.clear_canvas)
        self.clear_button.opacity = 0  # Initially hidden
        layout.add_widget(self.clear_button)
        
        # Add a back button with custom image
        self.back_button = Button(
            background_normal='assets/back_button.png',
            background_down='assets/back_button_pressed.png',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.9, 'y': 0.02}
        )
        self.back_button.bind(on_press=self.on_back_button_press)
        layout.add_widget(self.back_button)
        
        # Add a button for adding photos
        self.photo_button = Button(
            background_normal='assets/add_photo_button.png',
            background_down='assets/add_photo_button_pressed.png',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.02}
        )
        self.photo_button.bind(on_press=self.open_image_screen)
        layout.add_widget(self.photo_button)
        
        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def toggle_input_mode(self, instance):
        if self.doodle_widget.opacity == 0:
            self.doodle_widget.opacity = 1
            self.text_input.opacity = 0
            self.clear_button.opacity = 1
            self.toggle_button.background_normal = 'assets/switch_to_text_button.png'
            self.toggle_button.background_down = 'assets/switch_to_text_button_pressed.png'
        else:
            self.doodle_widget.opacity = 0
            self.text_input.opacity = 1
            self.clear_button.opacity = 0
            self.toggle_button.background_normal = 'assets/switch_to_doodle_button.png'
            self.toggle_button.background_down = 'assets/switch_to_doodle_button_pressed.png'

    def on_save_button_press(self, instance):
        # Save the journal entry to a file or variable
        journal_entry = self.text_input.text
        file_name = f'journal_entry_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
        file_path = os.path.join(os.getcwd(), 'saved_journals', file_name)
        with open(file_path, 'w') as file:
            file.write(journal_entry)
        print(f"Journal entry saved at {file_path}")

    def clear_canvas(self, instance):
        self.doodle_widget.clear_canvas()

    def on_back_button_press(self, instance):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='right')
        screen_manager.current = 'home'
    
    def open_image_screen(self, instance):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = 'image'



class DoodleWidget(Widget):
    def __init__(self, **kwargs):
        super(DoodleWidget, self).__init__(**kwargs)
        self.line = None

    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 0, 0)  # Set the drawing color to black
            self.line = Line(points=[touch.x, touch.y])

    def on_touch_move(self, touch):
        if self.line:
            self.line.points += [touch.x, touch.y]

    def clear_canvas(self):
        self.canvas.clear()

class DoodleScreen(Screen):
    def __init__(self, **kwargs):
        super(DoodleScreen, self).__init__(**kwargs)
        with self.canvas.before:
            self.rect = Rectangle(source='assets/journal_background.png', size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        layout = FloatLayout()
        
        # Add the DoodleWidget
        self.doodle_widget = DoodleWidget(size_hint=(0.8, 0.4), pos_hint={'center_x': 0.5, 'top': 0.8})
        layout.add_widget(self.doodle_widget)

        # Add a clear button with custom image
        self.clear_button = Button(
            background_normal='assets/clear_button.png',
            background_down='assets/clear_button_pressed.png',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.7, 'y': 0.02}
        )
        self.clear_button.bind(on_press=self.clear_canvas)
        layout.add_widget(self.clear_button)
        
        # Add a back button with custom image
        self.back_button = Button(
            background_normal='assets/back_button.png',
            background_down='assets/back_button_pressed.png',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.9, 'y': 0.02}
        )
        self.back_button.bind(on_press=self.on_back_button_press)
        layout.add_widget(self.back_button)
        
        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def clear_canvas(self, instance):
        self.doodle_widget.clear_canvas()

    def on_back_button_press(self, instance):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='right')
        screen_manager.current = 'journal'

class ImageScreen(Screen):
    def __init__(self, **kwargs):
        super(ImageScreen, self).__init__(**kwargs)

        layout = FloatLayout()

        self.background = Image(source='assets/journal_background.png', size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(self.background)

        # Add the image widget
        self.image_widget = Image(source='', size_hint=(0.8, 0.4), pos_hint={'center_x': 0.5, 'top': 0.8})
        layout.add_widget(self.image_widget)

        # Add a clear button
        self.clear_button = Button(
            background_normal='assets/clear_button.png',
            background_down='assets/clear_button_pressed.png',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.7, 'y': 0.02}
        )
        self.clear_button.bind(on_press=self.clear_image)
        layout.add_widget(self.clear_button)

        # Add a back button
        self.back_button = Button(
            background_normal='assets/back_button.png',
            background_down='assets/back_button_pressed.png',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.9, 'y': 0.02}
        )
        self.back_button.bind(on_press=self.on_back_button_press)
        layout.add_widget(self.back_button)

        # Add a switch to text button
        self.switch_to_text_button = Button(
            background_normal='assets/switch_to_text_button.png',
            background_down='assets/switch_to_text_button_pressed.png',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.02}
        )
        self.switch_to_text_button.bind(on_press=self.switch_to_text)
        layout.add_widget(self.switch_to_text_button)

        # Add a save button
        self.save_button = Button(
            background_normal='assets/save_button.png',
            background_down='assets/save_button_pressed.png',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.3, 'y': 0.02}
        )
        self.save_button.bind(on_press=self.save_image)
        layout.add_widget(self.save_button)

        # Add a button for adding photos
        self.photo_button = Button(
            background_normal='assets/add_photo_button.png',
            background_down='assets/add_photo_button_pressed.png',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.1, 'y': 0.02}
        )
        self.photo_button.bind(on_press=self.open_file_chooser)
        layout.add_widget(self.photo_button)

        self.add_widget(layout)

    def clear_image(self, instance):
        self.image_widget.source = ''

    def on_back_button_press(self, instance):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='right')
        screen_manager.current = 'home'

    def switch_to_text(self, instance):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = 'journal'

    def save_image(self, instance):
        # Save the image to a file
        image_path = self.image_widget.source
        if image_path:
            file_name = os.path.basename(image_path)
            destination = os.path.join(os.getcwd(), 'saved_images', file_name)
            try:
                with open(destination, 'wb') as dest:
                    with open(image_path, 'rb') as src:
                        dest.write(src.read())
                print(f"Image saved successfully at: {destination}")
            except Exception as e:
                print(f"Error occurred while saving image: {e}")
        else:
            print("No image to save.")

    def open_file_chooser(self, instance):
        # Open file chooser dialog to select an image
        file_chooser = FileChooserIconView(path='.', filters=['*.png', '*.jpg'])
        file_chooser.bind(on_submit=self.load_selected_image)
        popup = Popup(title="Select an Image", content=file_chooser, size_hint=(0.9, 0.9))
        popup.open()

    def load_selected_image(self, chooser, selection, touch):
        # Load the selected image into the image screen
        if selection:
            self.image_widget.source = os.path.join(chooser.path, selection[0])

class SavedJournalsScreen(Screen):
    def __init__(self, **kwargs):
        super(SavedJournalsScreen, self).__init__(**kwargs)
        with self.canvas.before:
            self.rect = Rectangle(source='assets/saved_background.png', size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        layout = FloatLayout()

        self.scrollview = ScrollView(size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.gridlayout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.gridlayout.bind(minimum_height=self.gridlayout.setter('height'))
        self.scrollview.add_widget(self.gridlayout)
        layout.add_widget(self.scrollview)

        self.back_button = Button(
            background_normal='assets/back_button.png',
            background_down='assets/back_button_pressed.png',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.02}
        )
        self.back_button.bind(on_press=self.on_back_button_press)
        layout.add_widget(self.back_button)

        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def add_journal_entry(self, journal_entry):
        entry_layout = GridLayout(cols=1, spacing=10, size_hint_y=None, height=200)
        entry_layout.add_widget(Label(text=f"Date: {journal_entry.date}", font_size='20sp'))
        entry_layout.add_widget(Label(text=f"Content: {journal_entry.content}", font_size='16sp'))
        self.gridlayout.add_widget(entry_layout)

    def on_back_button_press(self, instance):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='right')
        screen_manager.current = 'home'

class MyApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()

        # Add screens to the screen manager
        sm = ScreenManager()
        sm.add_widget(GetStartedScreen(name='get_started'))
        sm.add_widget(OnboardingScreen(name='screen1', bg_image='assets/background1.png'))
        sm.add_widget(OnboardingScreen(name='screen2', bg_image='assets/background2.png'))
        sm.add_widget(OnboardingScreen(name='screen3', bg_image='assets/background3.png'))
        sm.add_widget(OnboardingScreen(name='screen4', bg_image='assets/background4.png'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(JournalScreen(name='journal'))
        sm.add_widget(DoodleScreen(name='doodle'))
        sm.add_widget(ImageScreen(name='image'))
        sm.add_widget(AboutDeveloperScreen(name='about_developer'))
        sm.add_widget(SavedJournalsScreen(name='saved_journals'))


        return sm


if __name__ == '__main__':
    MyApp().run()


