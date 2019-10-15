class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 850
        self.bg_color = (0, 0, 0)

        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 237, 25, 2
        self.ship_bullet_color = 22, 2, 244
        self.bullets_allowed = 3

        self.fleet_drop_speed = 15

        self.speedup_scale = 1.1

        self.score_scale = 1.5

        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5

        self.alien_1_points = 10
        self.alien_2_points = 20
        self.alien_3_points = 40

        self.fleet_direction = 1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5

        self.alien_1_points = 10
        self.alien_2_points = 20
        self.alien_3_points = 40

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
