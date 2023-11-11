import matplotlib.pyplot as plt

class Aircraft:
    def __init__(self, mass, engine_thrust, drag_coefficient, lift_coefficient):
        self.mass = mass
        self.engine_thrust = engine_thrust
        self.drag_coefficient = drag_coefficient
        self.lift_coefficient = lift_coefficient

    def kinetic_energy(self, velocity):
        return 0.5 * self.mass * velocity**2

    def potential_energy(self, altitude):
        g = 9.81  # Acceleration due to gravity (m/s^2)
        return self.mass * g * altitude

    def update_velocity(self, velocity, time_step):
        drag_force = 0.5 * self.drag_coefficient * velocity**2
        net_force = self.engine_thrust - drag_force
        acceleration = net_force / self.mass
        new_velocity = velocity + acceleration * time_step
        return new_velocity

    def turn_rate(self, velocity):
        # Simplified turn rate calculation
        # Higher speed usually means a lower turn rate
        return self.lift_coefficient / (velocity * self.drag_coefficient)

    def turn_radius(self, velocity):
        # Simplified turn radius calculation
        # Higher speed usually means a larger turn radius
        return velocity**2 / (self.lift_coefficient * 9.81)

    def update_orientation(self, velocity, time_step, turning):
        if turning:
            rate = self.turn_rate(velocity)
            angle_change = rate * time_step  # Change in orientation in radians
        else:
            angle_change = 0
        return angle_change  # You can later expand this to update the aircraft's actual orientation



# import matplotlib.pyplot as plt
# import numpy as np

# # Define a range of speed values (arbitrary units)
# speeds = np.linspace(100, 900, 800)

# # Example energy profile of a fighter jet
# # Potential energy will be modelled as a constant in this example, focusing on kinetic energy
# kinetic_energy = 0.5 * speeds**2  # Kinetic energy = 1/2 * mass * velocity^2, mass is constant

# # Turn rate - assuming it increases with speed up to a point, then decreases
# optimal_turn_speed = 450
# turn_rate = 1 / (0.001 * (speeds - optimal_turn_speed)**2 + 1)  # Inverse parabolic function

# # Turn radius - assuming it decreases with speed up to a point, then increases
# optimal_turn_radius_speed = 350
# turn_radius = 0.005 * (speeds - optimal_turn_radius_speed)**2 + 0.5  # Parabolic function

# # Create plots
# plt.figure(figsize=(15, 5))

# # Kinetic energy plot
# plt.subplot(1, 3, 1)
# plt.plot(speeds, kinetic_energy, color='blue')
# plt.title('Kinetic Energy vs Speed')
# plt.xlabel('Speed')
# plt.ylabel('Kinetic Energy')

# # Turn rate plot
# plt.subplot(1, 3, 2)
# plt.plot(speeds, turn_rate, color='green')
# plt.title('Turn Rate vs Speed')
# plt.xlabel('Speed')
# plt.ylabel('Turn Rate')

# # Turn radius plot
# plt.subplot(1, 3, 3)
# plt.plot(speeds, turn_radius, color='red')
# plt.title('Turn Radius vs Speed')
# plt.xlabel('Speed')
# plt.ylabel('Turn Radius')

# plt.tight_layout()
# plt.show()
