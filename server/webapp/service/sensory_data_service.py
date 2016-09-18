import os
import config as CONFIG

class SensoryDataService:
    def handle_smartphone_sensory_data(self, activity_type, sensory_data):
        accelerometer_data = sensory_data['accelerometer']
        barometer_data = sensory_data['barometer']
        gravity_data = sensory_data['gravity']
        gyroscope_data = sensory_data['gyroscope']
        linear_accelerometer_data = sensory_data['linearAccelerometer']
        magnetic_data = sensory_data['magnetic']

        self.store_smartphone_file(activity_type, CONFIG.ACCELEROMETER_RESULT_SMARTPHONE, accelerometer_data)
        self.store_smartphone_file(activity_type, CONFIG.BAROMETER_RESULT_SMARTPHONE, barometer_data)
        self.store_smartphone_file(activity_type, CONFIG.GRAVITY_RESULT_SMARTPHONE, gravity_data)
        self.store_smartphone_file(activity_type, CONFIG.GYROSCOPE_RESULT_SMARTPHONE, gyroscope_data)
        self.store_smartphone_file(activity_type, CONFIG.LINEAR_ACCELEROMETER_RESULT_SMARTPHONE, linear_accelerometer_data)
        self.store_smartphone_file(activity_type, CONFIG.MAGNETIC_RESULT_SMARTPHONE, magnetic_data)


    def handle_smartwatch_sensory_data(self, activity_type, sensory_data):
        accelerometer_data = self.convert_smartwatch_accelerometer_data_to_csv(sensory_data['accelerometer']['data'])
        gyroscope_data = self.convert_smartwatch_gyroscope_data_to_csv(sensory_data['gyroscope']['data'])
        light_data = self.convert_smartwatch_light_data_to_csv(sensory_data['light']['data'])
        pressure_data = self.convert_smartwatch_pressure_data_to_csv(sensory_data['pressure']['data'])
        magnetic_data = self.convert_smartwatch_magnetic_data_to_csv(sensory_data['magnetic']['data'])
        uv_data = self.convert_smartwatch_ultraviolet_data_to_csv(sensory_data['uv']['data'])

        self.store_smartwatch_file(activity_type, CONFIG.ACCELEROMETER_RESULT_SMARTWATCH, accelerometer_data)
        self.store_smartwatch_file(activity_type, CONFIG.GYROSCOPE_RESULT_SMARTWATCH, gyroscope_data)
        self.store_smartwatch_file(activity_type, CONFIG.LIGHT_RESULT_SMARTWATCH, light_data)
        self.store_smartwatch_file(activity_type, CONFIG.PRESSURE_RESULT_SMARTWATCH, pressure_data)
        self.store_smartwatch_file(activity_type, CONFIG.MAGNETIC_RESULT_SMARTWATCH, magnetic_data)
        self.store_smartwatch_file(activity_type, CONFIG.ULTRAVIOLET_RESULT_SMARTWATCH, uv_data)


    def store_smartphone_file(self, activity_type, file_name, file_content):
        self.create_activity_directory(activity_type)

        f = open(os.path.join(CONFIG.RAW_DATA_DIR, activity_type, file_name), 'w')
        f.write(file_content)
        f.close()


    def store_smartwatch_file(self, activity_type, file_name, file_content):
        self.create_activity_directory(activity_type)

        f = open(os.path.join(CONFIG.RAW_DATA_DIR, activity_type, file_name), 'w')
        f.write(file_content)
        f.close()


    def create_activity_directory(self, activity_type):
        dir_path = os.path.join(CONFIG.RAW_DATA_DIR, activity_type)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)


    def convert_smartwatch_accelerometer_data_to_csv(self, accelerometer_data):
        result_list = []
        for a in accelerometer_data:
            result_list.append('{},{},{},{}'.format(a['timestamp'], a['ax'], a['ay'], ['az']))

        return '\n'.join(result_list)


    def convert_smartwatch_gyroscope_data_to_csv(self, gyroscope_data):
        result_list = []
        for g in gyroscope_data:
            result_list.append('{},{},{},{}'.format(g['timestamp'], g['gx'], g['gy'], g['gz']))

        return '\n'.join(result_list)


    def convert_smartwatch_light_data_to_csv(self, light_data):
        result_list = []
        for l in light_data:
            result_list.append('{},{}'.format(l['timestamp'], l['light']))

        return '\n'.join(result_list)


    def convert_smartwatch_pressure_data_to_csv(self, pressure_data):
        result_list = []
        for p in pressure_data:
            result_list.append('{},{}'.format(p['timestamp'], p['pressure']))

        return '\n'.join(result_list)


    def convert_smartwatch_magnetic_data_to_csv(self, magnetic_data):
        result_list = []
        for m in magnetic_data:
            result_list.append('{},{},{},{},{}'.format(
                m['timestamp'],
                m['mx'],
                m['my'],
                m['mz'],
                m['mAcc']
            ))

        return '\n'.join(result_list)


    def convert_smartwatch_ultraviolet_data_to_csv(self, ultraviolet_data):
        result_list = []
        for u in ultraviolet_data:
            result_list.append('{},{}'.format(u['timestamp'], u['uv']))

        return '\n'.join(result_list)