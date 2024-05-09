import wx
from PIL import Image
import os


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(400, 400))

        panel = wx.Panel(self)
        wx.StaticText(panel, label="Drag and drop image file here", pos=(60, 60))

        self.resize_checkbox = wx.CheckBox(panel, label="Resize Image?", pos=(60, 160))
        self.resize_checkbox.Bind(wx.EVT_CHECKBOX, self.on_resize_check)

        self.width_title = wx.StaticText(panel, label="Resize Width:", pos=(60, 200))
        self.height_title = wx.StaticText(panel, label="Resize Height:", pos=(60, 230))

        self.width_text_ctrl = wx.TextCtrl(panel, value="2560", pos=(140, 200), size=(60, -1))
        self.height_text_ctrl = wx.TextCtrl(panel, value="1920", pos=(140, 230), size=(60, -1))

        # Quality slider
        wx.StaticText(panel, label="JPEG Quality:", pos=(60, 110))
        self.quality_slider = wx.Slider(panel, value=95, minValue=0, maxValue=100, pos=(140, 110), size=(150, -1),
                                        style=wx.SL_HORIZONTAL | wx.SL_LABELS)

        # Initially hide the width and height options
        self.width_title.Hide()
        self.height_title.Hide()
        self.width_text_ctrl.Hide()
        self.height_text_ctrl.Hide()

        drop_target = MyFileDropTarget(self)
        panel.SetDropTarget(drop_target)

        self.Centre()
        self.Bind(wx.EVT_CLOSE, self.on_close_window)
        self.Show(True)

    def on_resize_check(self, event):
        # Show or hide the resize controls based on the checkbox state
        show = self.resize_checkbox.GetValue()
        self.width_title.Show(show)
        self.height_title.Show(show)
        self.width_text_ctrl.Show(show)
        self.height_text_ctrl.Show(show)

        # Ensure controls are shown/hidden correctly
        self.Layout()

    def on_close_window(self, event):
        self.Destroy()


class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):
        for index, filename in enumerate(filenames):
            img = Image.open(filename)
            img = img.convert('RGB')  # Strip alpha channel if present, to remove EXIF data

            # Resize the image if the resize option is enabled
            if self.window.resize_checkbox.GetValue():
                width = int(self.window.width_text_ctrl.GetValue())
                height = int(self.window.height_text_ctrl.GetValue())
                img = img.resize((width, height), Image.Resampling.LANCZOS)

            # Get the quality value
            quality = self.window.quality_slider.GetValue()

            base, ext = os.path.splitext(filename)
            new_filename = f"{base}_edit{ext}"

            img.save(new_filename, 'JPEG', quality=quality)

            # Log each processed file
            print(f"Processed file: {new_filename} with quality {quality}")

        wx.MessageBox("All photos have been processed successfully!", "Process Complete", wx.OK | wx.ICON_INFORMATION)

        return True


if __name__ == '__main__':
    app = wx.App(False)
    Mywin(None, 'Image Processor')
    app.MainLoop()
