import subprocess,time

seconds = 0.01
def coords_finder(seconds): # -- Shows a monitor coords
    while True:
        coords = subprocess.run(
            [
                "hyprctl", "cursorpos"#cursor-pos
            ], capture_output = True, text = True#outputs
        )
        clean_coords = coords.stdout.strip()#cleaning "_...(strips)"
        print(f":, {clean_coords:<30}", end = "\r", flush = True)
        time.sleep(seconds)

coords_finder(seconds)