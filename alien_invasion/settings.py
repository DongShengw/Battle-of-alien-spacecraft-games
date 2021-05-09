class Settings():
	"""储存《外星人入侵》的所有设置的类"""
	
	def __init__(self):
		"""初始化游戏的静态设置"""
		#屏幕设置
		self.screen_width = 750 #屏幕长
		self.screen_height=  600 #屏幕宽
		self.bg_color=(0,0,0) #颜色
		
		#飞船参数设置
		self.ship_limit = 2
		
		#子弹
		self.bullet_width = 300
		self.bullet_height = 6
		self.bullet_color = 160,160,160
		self.bullets_allowed = 20

		#外星人
		self.fleet_drop_speed = 2

		#计分
		self.alien_points = 50
		
		#以什么样的速度加速游戏节奏
		self.speedup_scale = 1.1
		
		#外星人点数的提高速度
		self.score_scale = 1.5
		
		self.initialize_dynamic_settings()
	
	def initialize_dynamic_settings(self):
		"""初始化随游戏进行而变化的设置"""
		self.ship_speed_factor = 1.3
		self.bullet_speed_factor = 2
		self.alien_speed_factor = 0.5
		
		#fleet_direction 为1表示向右， -1 表示向左
		self.fleet_direction = 1
	
	def increase_speed(self):
		"""提高速度设置和外星人点数"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale 
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		#print(self.alien_points)
