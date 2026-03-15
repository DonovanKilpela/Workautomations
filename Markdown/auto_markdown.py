import customtkinter as ctk


def main():
    # ---- CustomTkinter global settings ----
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.title("Markdown List Automation")
    app.geometry("900x550")
    app.minsize(700, 450)

    # Grid config for main window
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=0)   # top (mode selector)
    app.rowconfigure(1, weight=1)   # middle (content frames)
    app.rowconfigure(2, weight=1)   # output frame
    app.rowconfigure(3, weight=0)   # bottom (buttons)

    # =========================
    #  MODE SELECTION (TOP)
    # =========================
    mode_var = ctk.StringVar(value="Permissions Lost")

    def on_mode_change(choice):
        show_mode(choice)

    mode_frame = ctk.CTkFrame(app, corner_radius=10)
    mode_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
    mode_frame.grid_columnconfigure(0, weight=0)
    mode_frame.grid_columnconfigure(1, weight=1)

    mode_label = ctk.CTkLabel(
        mode_frame,
        text="Select Markdown Type:",
        font=ctk.CTkFont(size=14, weight="bold"),
    )
    mode_label.grid(row=0, column=0, padx=10, pady=8, sticky="w")

    mode_menu = ctk.CTkOptionMenu(
        mode_frame,
        variable=mode_var,
        values=["Permissions Lost", "Cross Train Tickets"],
        command=on_mode_change,
        width=220,
    )
    mode_menu.grid(row=0, column=1, padx=10, pady=8, sticky="e")

    # =========================
    #  CONTENT CONTAINER
    # =========================
    content_container = ctk.CTkFrame(app, corner_radius=10)
    content_container.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsew")
    content_container.grid_columnconfigure(0, weight=1)
    content_container.grid_rowconfigure(0, weight=1)

    # We will keep modes frames in a dict and raise the selected one.
    mode_frames = {}

    # =======================================================
    #  MODE 1: PERMISSIONS LOST 
    # =======================================================
    perm_frame = ctk.CTkFrame(content_container, corner_radius=10)
    perm_frame.grid(row=0, column=0, sticky="nsew")
    perm_frame.grid_columnconfigure(0, weight=1)

    # ---- Frame for rows of people ----
    people_frame = ctk.CTkFrame(perm_frame, corner_radius=10)
    people_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Title label for people_frame
    people_title = ctk.CTkLabel(
        people_frame,
        text="Permissions Lost",
        font=ctk.CTkFont(size=16, weight="bold"),
    )
    people_title.grid(row=0, column=0, columnspan=4, sticky="w", pady=(5, 10), padx=5)

    # Header labels
    headers = ["Login", "Cohort", "Manager", "Permission"]
    for col, text in enumerate(headers):
        lbl = ctk.CTkLabel(
            people_frame, text=text, font=ctk.CTkFont(size=13, weight="bold")
        )
        lbl.grid(row=1, column=col, padx=4, pady=(0, 4), sticky="w")

    # Allow columns to stretch
    for col in range(4):
        people_frame.grid_columnconfigure(col, weight=1)

    # Store all row widgets so we can iterate over them later
    perm_person_rows = []

    def add_person_row():
        row_index = len(perm_person_rows) + 2  # 0 is title, 1 is header row

        login_entry = ctk.CTkEntry(people_frame, placeholder_text="Login")
        login_entry.grid(row=row_index, column=0, padx=4, pady=4, sticky="ew")

        cohort_entry = ctk.CTkEntry(people_frame, placeholder_text="Cohort")
        cohort_entry.grid(row=row_index, column=1, padx=4, pady=4, sticky="ew")  

        manager_entry = ctk.CTkEntry(people_frame, placeholder_text="Manager")
        manager_entry.grid(row=row_index, column=2, padx=4, pady=4, sticky="ew")

        permission_entry = ctk.CTkEntry(people_frame, placeholder_text="Permission")
        permission_entry.grid(row=row_index, column=3, padx=4, pady=4, sticky="ew")

        # Store entries as a tuple in the list
        perm_person_rows.append(
            (permission_entry, login_entry, cohort_entry, manager_entry)
        )

    mode_frames["Permissions Lost"] = perm_frame

    # =======================================================
    #  MODE 2: CROSS TRAIN TICKETS 
    # =======================================================
    ct_frame = ctk.CTkFrame(content_container, corner_radius=10)
    ct_frame.grid(row=0, column=0, sticky="nsew")

    ct_title = ctk.CTkLabel(
        ct_frame,
        text="Cross Train Tickets",
        font=ctk.CTkFont(size=16, weight="bold"),
    )
    ct_title.grid(row=0, column=0, columnspan=4, sticky="w", pady=(5, 10), padx=5)

    ct_headers = ["Home Area", "Login", "Manager", "Cohort", "Cross Train Department"]
    for col, text in enumerate(ct_headers):
        lbl = ctk.CTkLabel(
            ct_frame, text=text, font=ctk.CTkFont(size=13, weight="bold")
        )
        lbl.grid(row=1, column=col, padx=4, pady=(0, 4), sticky="w")

    for col in range(4):
        ct_frame.grid_columnconfigure(col, weight=1)

    ct_rows = []

    def add_ct_row():
        row_index = len(ct_rows) + 2

        home_area_entry = ctk.CTkEntry(ct_frame, placeholder_text="Home Area")
        home_area_entry.grid(row=row_index, column=0, padx=4, pady=4, sticky="ew")

        login_entry = ctk.CTkEntry(ct_frame, placeholder_text="Login")
        login_entry.grid(row=row_index, column=1, padx=4, pady=4, sticky="ew")

        manager_entry = ctk.CTkEntry(ct_frame, placeholder_text="Manager")
        manager_entry.grid(row=row_index, column=2, padx=4, pady=4, sticky="ew")

        cohort_entry = ctk.CTkEntry(ct_frame, placeholder_text="Cohort")
        cohort_entry.grid(row=row_index, column=3, padx=2, pady=2, sticky="ew")

        xt_department_entry = ctk.CTkEntry(ct_frame, placeholder_text="Cross Train Department")
        xt_department_entry.grid(row=row_index, column=4, padx=4, pady=4, sticky="ew")

        ct_rows.append((home_area_entry, login_entry, manager_entry, cohort_entry, xt_department_entry))

    mode_frames["Cross Train Tickets"] = ct_frame

    
    # =======================================================
    #  MODE 3: RETRAIN TICKETS 
    # =======================================================


    # =======================================================
    #  OUTPUT FRAME (shared)
    # =======================================================
    output_frame = ctk.CTkFrame(app, corner_radius=10)
    output_frame.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="nsew")
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

    # =======================================================
    #  GENERATE FUNCTIONS PER MODE
    # =======================================================
    def generate_permissions_lost():
        lines = [
            "| Permission | Login | Cohort | Manager |",
            "|------------|-------|--------|---------|",
        ]

        for permission_entry, login_entry, cohort_entry, manager_entry in perm_person_rows:
            permission = permission_entry.get().strip()
            login = login_entry.get().strip()
            cohort = cohort_entry.get().strip()
            manager = manager_entry.get().strip()

            # Skip blank rows
            if not (permission or cohort or login or manager):
                continue

            lines.append(f"| {permission} | {login} | {cohort} | {manager} |")

        return "\n".join(lines)

    def generate_cross_train():
        lines = [
            "| Home Area | Login | Manager | Cohort | Cross Train Department |",
            "|-----------|-------|---------|--------|------------------------|",
        ]

        for home_area_entry, login_entry, manager_entry, cohort_entry, xt_department_enrty in ct_rows:
            home_area = home_area_entry.get().strip()
            login = login_entry.get().strip()
            manager = manager_entry.get().strip()
            cohort = cohort_entry.get().strip()
            xt_department = xt_department_enrty.get().strip()

            if not (home_area or login or manager or cohort or xt_department):
                continue

            lines.append(f"| {home_area} | {login} | {manager} | {cohort} | {xt_department} |")

        return "\n".join(lines)

    def generate_markdown():
        mode = mode_var.get()
        if mode == "Permissions Lost":
            markdown_output = generate_permissions_lost()
        else:
            markdown_output = generate_cross_train()

        output_textbox.configure(state="normal")
        output_textbox.delete("1.0", "end")
        output_textbox.insert("1.0", markdown_output)
        output_textbox.configure(state="disabled")

    # =======================================================
    #  BUTTONS (bottom)
    # =======================================================
    buttons_frame = ctk.CTkFrame(app, corner_radius=10)
    buttons_frame.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="ew")
    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)
    buttons_frame.grid_columnconfigure(2, weight=1)

    def add_row_for_current_mode():
        mode = mode_var.get()
        if mode == "Permissions Lost":
            add_person_row()
        else:
            add_ct_row()

    add_button = ctk.CTkButton(
        buttons_frame,
        text="Add Row",
        command=add_row_for_current_mode,
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

    # =======================================================
    #  FRAME SWITCHING
    # =======================================================
    def show_mode(name: str):
        # stack both frames in the same grid cell, raise the selected one
        perm_frame.grid(row=0, column=0, sticky="nsew")
        ct_frame.grid(row=0, column=0, sticky="nsew")
        mode_frames[name].tkraise()

    # Start with one row for each mode (optional)
    add_person_row()
    add_ct_row()

    # Show default mode
    show_mode(mode_var.get())

    app.mainloop()


if __name__ == "__main__":
    main()
