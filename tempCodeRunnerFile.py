canvas = Canvas(window, bg='#423C34', width=800, height=600)
# scrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)
# scrollable_frame = Frame(canvas, bg='#423C34')

# scrollable_frame.bind(
#     "<Configure>",
#     lambda e: canvas.configure(
#         scrollregion=canvas.bbox("all")
#     )
# )

# canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# canvas.configure(yscrollcommand=scrollbar.set)

# canvas.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="right", fill="y")

# def _on_mousewheel(event):
#     canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# canvas.bind_all("<MouseWheel>", _on_mousewheel)

