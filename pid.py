class PID():
    def __init__ (self, k_p_1, k_i_1, k_d_1, k_p_2, k_i_2, k_d_2):
        self.k_p_1 = k_p_1
        self.k_i_1 = k_i_1
        self.k_d_1 = k_d_1

        self.k_p_2 = k_p_2
        self.k_i_2 = k_i_2
        self.k_d_2 = k_d_2
        self.error_1 = 0
        self.error_2 = 0

    def act (self, observation):
        cart_pos, cart_pos_dot, pole_angle, pole_angle_dot = observation

        self.error_1 += cart_pos
        self.error_2 += pole_angle

        ans1 = self.k_p_1 * cart_pos + self.k_i_1 * self.error_1 + self.k_d_1 * cart_pos_dot
        ans2 = self.k_p_2 * pole_angle + self.k_i_2 * self.error_2 + self.k_d_2 * pole_angle_dot

        ans = ans1 + ans2
        return 1 if ans > 0 else 0
