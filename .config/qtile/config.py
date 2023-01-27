import os
import subprocess
from libqtile import qtile, bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras.widget.decorations import PowerLineDecoration


import colors

home = os.path.expanduser('~')
mod = "mod4"
terminal = "konsole"  # guess_terminal()
browser = "firefox"
file_launcher1 = 'rofi -show drun'
file_launcher2 = 'rofi -show run'
touchpad_command = 'xinput --set-prop "ELAN2204:00 04F3:3109 Touchpad" "libinput Natural Scrolling Enabled" 1'    


mbfs = colors.mbfs()
doomOne = colors.doomOne()
dracula = colors.dracula()
everforest = colors.everforest()
nord = colors.nord()
gruvbox = colors.gruvbox()

# Choose colorscheme
colorscheme = nord

# Colorschme funcstion
colors, backgroundColor, foregroundColor, workspaceColor, foregroundColorTwo = colorscheme 



keys = [
    # media keys
    Key([], "XF86AudioLowerVolume", lazy.widget["volume"].decrease_vol(), desc="decrease volume"),
    Key([], "XF86AudioRaiseVolume", lazy.widget["volume"].increase_vol(), desc="increase volume"),
    Key([], "XF86AudioMute", lazy.widget["volume"].mute(), desc="mute volume"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +5%"), desc="increase brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-"), desc="decrease brightness"),

    # Power menu
    Key([mod], "q", lazy.spawn("powermenu")),

    # Toggle bar
    Key([mod], "p", lazy.hide_show_bar(), desc="toggle the bar"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # launch programs
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc = "Launch browser"),
    Key([mod], "Return", lazy.spawn(file_launcher1), desc = "Launch primary launcher"),
    Key([mod, "shift"], "Return", lazy.spawn(file_launcher2), desc = "Launch secondary launcher"),
]


group_names = [("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]


for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group




layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(border_focus='#7e618c', margin=0),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

powerline = {
    "decorations": [
        PowerLineDecoration(path="arrow_right")
    ]
}

widget_defaults = dict(
    font="FiraMono",
    fontsize=16,
    padding=3,
    background=backgroundColor,
)
extension_defaults = widget_defaults.copy()
c1 = "#1f285d"
c2 = "#4b849a"
# colors, backgroundColor, foregroundColor, workspaceColor, foregroundColorTwo = colorscheme 
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method="block",
                    fontsize=24,
                    padding=10,
                    active="ffffff",
                    background=backgroundColor,
                    this_current_screen_border=workspaceColor,
                    this_screen_border=workspaceColor,
                    ),
                widget.CurrentLayout(),
                widget.Prompt(),
                widget.WindowName(format='{state}', **powerline),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                    **powerline
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(**powerline),
                widget.Backlight(brightness_file="/sys/class/backlight/amdgpu_bl0/actual_brightness", max_brightness_file="/sys/class/backlight/amdgpu_bl0/max_brightness", fmt='盛 {}', background=c1, **powerline),
                widget.Memory(measure_mem='G', fmt = 'Mem: {}', 
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                    background=c2, **powerline
                    ),
                widget.Volume(fmt='{}  ', background=c1, **powerline), 
                widget.Battery(format='{percent:2.0%}  ', background=c2, **powerline),
                widget.Clock(format="  %a %d/%m |  %H:%M", background=c1, padding=7, **powerline), #"%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(default_text='[X]', countdown_format='[{}]', padding=7),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

@hook.subscribe.startup_once
def start_once():
    subprocess.call([home + '/.config/qtile/autostart.sh'])

@hook.subscribe.startup
def startup():
    qtile.cmd_hide_show_bar('all')
    

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
