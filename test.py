import dearpygui.dearpygui as dpg

def add_log(message):
    dpg.add_text(message, parent=log_group)

def task_clicked(sender, app_data):
    print(sender)
    print(app_data)
    task_name = dpg.get_item_label(sender)
    add_log(f"Task '{task_name}' selected")

dpg.create_context()

# 创建主窗口，并指定 tag "MainWindow"
with dpg.window(label="Task Manager", width=640, height=400, tag="MainWindow"):
    with dpg.group(horizontal=True):
        with dpg.child_window(width=200, height=380, label="Tasks"):
            dpg.add_button(label="Task 1", callback=task_clicked, tag="TSK")
            dpg.add_button(label="中文测试", callback=task_clicked, tag="test")
            dpg.add_button(label="Task 3", callback=task_clicked)
            dpg.add_button(label="Task 4", callback=task_clicked)
            dpg.add_button(label="Task 5", callback=task_clicked)
        
        with dpg.child_window(width=400, height=380, label="Logs"):
            log_group = dpg.add_group()

# 设置主窗口为 "MainWindow"
dpg.set_primary_window("MainWindow", True)

dpg.create_viewport(title="Task Manager", width=640, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
