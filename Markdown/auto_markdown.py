import customtkinter as ctk


def main():
    # ---- CustomTkinter global settings ----
    ctk.set_appearance_mode("light")          
    ctk.set_default_color_theme("green")  

    app = ctk.CTk()
    app.title("Permissions Lost Markdown Syntax Automation")
    app.geometry("900x550")
    app.minsize(700, 450)

    # Grid config for main window
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)   # top (people frame)
    app.rowconfigure(1, weight=1)   # middle (output frame)
    app.rowconfigure(2, weight=0)   # bottom (buttons)

    # ---- Frame for rows of people ----
    people_frame = ctk.CTkFrame(app, corner_radius=10)
    people_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Title label for people_frame
    people_title = ctk.CTkLabel(
        people_frame,
        text="People",
        font=ctk.CTkFont(size=16, weight="bold"),
    )
    people_title.grid(row=0, column=0, columnspan=4, sticky="w", pady=(5, 10), padx=5)

    # Header labels
    headers = ["Name", "Login", "Manager", "Permission"]
    for col, text in enumerate(headers):
        lbl = ctk.CTkLabel(
            people_frame, text=text, font=ctk.CTkFont(size=13, weight="bold")
        )
        lbl.grid(row=1, column=col, padx=4, pady=(0, 4), sticky="w")

    # Allow columns to stretch
    for col in range(4):
        people_frame.grid_columnconfigure(col, weight=1)

    # Store all row widgets so we can iterate over them later
    person_rows = []

    def add_person_row():
        row_index = len(person_rows) + 2  # 0 is title, 1 is header row

        name_entry = ctk.CTkEntry(people_frame, placeholder_text="Name")
        name_entry.grid(row=row_index, column=0, padx=4, pady=4, sticky="ew")

        login_entry = ctk.CTkEntry(people_frame, placeholder_text="Login")
        login_entry.grid(row=row_index, column=1, padx=4, pady=4, sticky="ew")

        manager_entry = ctk.CTkEntry(people_frame, placeholder_text="Manager")
        manager_entry.grid(row=row_index, column=2, padx=4, pady=4, sticky="ew")

        permission_entry = ctk.CTkEntry(people_frame, placeholder_text="Permission")
        permission_entry.grid(row=row_index, column=3, padx=4, pady=4, sticky="ew")

        # Store entries as a tuple in the list
        person_rows.append(
            (permission_entry, name_entry, login_entry, manager_entry)
        )

    # ---- Output frame ----
    output_frame = ctk.CTkFrame(app, corner_radius=10)
    output_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")
    output_frame.grid_rowconfigure(1, weight=1)
    output_frame.grid_columnconfigure(0, weight=1)

    output_label = ctk.CTkLabel(
        output_frame,
        text="Generated Markdown",
        font=ctk.CTkFont(size=16, weight="bold"),
    )
    output_label.grid(row=0, column=0, sticky="w", padx=10, pady=(8, 4))

    output_textbox = ctk.CTkTextbox(
        output_frame,
        width=400,
        height=150,
        wrap="word",
    )
    output_textbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    def generate_markdown():
        lines = [
            "| Permission | Name | Login | Manager |",
            "|-----------|------|-------|---------|",
        ]

        for permission_entry, name_entry, login_entry, manager_entry in person_rows:
            permission = permission_entry.get().strip()
            name = name_entry.get().strip()
            login = login_entry.get().strip()
            manager = manager_entry.get().strip()

            # Skip blank rows
            if not (permission or name or login or manager):
                continue

            lines.append(f"| {permission} | {name} | {login} | {manager} |")

        markdown_output = "\n".join(lines)

        output_textbox.configure(state="normal")
        output_textbox.delete("1.0", "end")
        output_textbox.insert("1.0", markdown_output)
        output_textbox.configure(state="disabled")

    # ---- Buttons frame ----
    buttons_frame = ctk.CTkFrame(app, corner_radius=10)
    buttons_frame.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="ew")
    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)
    buttons_frame.grid_columnconfigure(2, weight=1)

    add_button = ctk.CTkButton(
        buttons_frame,
        text="Add Person",
        command=add_person_row,
    )
    add_button.grid(row=0, column=0, padx=5, pady=8, sticky="ew")

    gen_button = ctk.CTkButton(
        buttons_frame,
        text="Generate Markdown",
        command=generate_markdown,
    )
    gen_button.grid(row=0, column=1, padx=5, pady=8, sticky="ew")

    
    def toggle_mode():
        current = ctk.get_appearance_mode().lower()
        ctk.set_appearance_mode("light" if current == "dark" else "dark")

    mode_button = ctk.CTkButton(
        buttons_frame,
        text="Toggle Light/Dark",
        command=toggle_mode,
    )
    mode_button.grid(row=0, column=2, padx=5, pady=8, sticky="ew")

    # Start with one empty row
    add_person_row()

    app.mainloop()


if __name__ == "__main__":
    main()
 