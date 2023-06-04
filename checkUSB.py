import wmi

# 获取USB控制器设备ID前缀
def get_usb_controller_prefix():
    c = wmi.WMI()
    controllers = c.Win32_USBController()
    controller_prefixes = []
    for controller in controllers:
        controller_prefixes.append(controller.DeviceID.split('\\')[0])
    return controller_prefixes

# 获取已连接的USB设备ID
def get_connected_usb_devices():
    c = wmi.WMI()
    connected_devices = []
    for device in c.Win32_PnPEntity():
        if 'USB' in device.DeviceID:
            connected_devices.append(device.DeviceID)
    return connected_devices

# 禁止指定设备使用
def disable_usb_device(device_id):
    c = wmi.WMI()
    for device in c.Win32_USBControllerDevice():
        if device.Dependent.endswith(device_id):
            device_name = device.Dependent.split('"')[-2]
            if 'USB Root Hub' not in device_name:
                print(f'Disabling device: {device_name}')
                dev = c.get(device.Antecedent.split('.')[1])
                dev.Disable()

# 获取USB控制器设备ID前缀
controller_prefixes = get_usb_controller_prefix()

# 获取已连接的USB设备ID
connected_devices = get_connected_usb_devices()

# 禁止所有非键盘鼠标设备的使用
for device_id in connected_devices:
    is_keyboard_or_mouse = False
    for prefix in controller_prefixes:
        if device_id.startswith(prefix):
            is_keyboard_or_mouse = True
            break
    if not is_keyboard_or_mouse:
        disable_usb_device(device_id)
