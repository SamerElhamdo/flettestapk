import flet as ft

def main(page: ft.Page):
    # تعيين عنوان التطبيق وحجمه
    page.title = "قائمة المهام"
    page.window_width = 400
    page.window_height = 600
    page.theme_mode = "light"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # إنشاء حقل إدخال المهمة الجديدة
    new_task = ft.TextField(
        hint_text="أضف مهمة جديدة",
        expand=True,
        text_align=ft.TextAlign.RIGHT
    )

    # قائمة المهام
    tasks = ft.Column()

    def add_task(e):
        if new_task.value:
            # إنشاء صف جديد للمهمة
            task_row = ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Checkbox(label=new_task.value),
                    ft.IconButton(
                        icon=ft.icons.DELETE_OUTLINE,
                        icon_color="red",
                        on_click=lambda e, row=task_row: delete_task(e, row)
                    )
                ]
            )
            tasks.controls.append(task_row)
            new_task.value = ""
            page.update()

    def delete_task(e, task_row):
        tasks.controls.remove(task_row)
        page.update()

    # إنشاء زر إضافة المهمة
    add_button = ft.IconButton(
        icon=ft.icons.ADD_CIRCLE,
        icon_color="blue",
        icon_size=40,
        on_click=add_task
    )

    # إضافة عناصر التحكم إلى الصفحة
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("قائمة المهام", size=32, weight=ft.FontWeight.BOLD),
                    ft.Row(
                        controls=[
                            new_task,
                            add_button
                        ]
                    ),
                    tasks
                ],
                spacing=20
            ),
            padding=20
        )
    )

ft.app(target=main)
