'''
An implementation of Runge-Kutta 4th order numerical integration, to estimate
position and velocity with respect to time and given acceleration. In this
example, acceleration is constant as only gravity is accounted for, but can
be varied as a function of force and mass.
'''


# initial params
position = 9.81 # [m]
velocity = 0.0 # [m/s]
acceleration = -9.81 # [m/s^2]
timestep = 0.01 # [ms]
duration = 1.0 # [s]



class State(object):

    def __init__(self, x = 0, v = 0):
        self.x = x  # position
        self.v = v  # velocity


class Derivative(object):

    def __init__(self, dx = 0, dv = 0):
        self.dx = dx    # velocity
        self.dv = dv    # acceleration



def eval(initial, accel, dt, d):

    state = State()
    state.x = initial.x + d.dx * dt
    state.v = initial.v + d.dv * dt

    output = Derivative()
    output.dx = state.v
    output.dv = accel

    return output



def rk4(state, dv, dt):
    ''' Implements Runge-Kutta 4th order numerical integration.'''

    a = eval(state, dv, dt, Derivative())
    b = eval(state, dv, dt*0.5, a)
    c = eval(state, dv, dt*0.5, b)
    d = eval(state, dv, dt, c)

    dxdt = ( a.dx + 2.0 * ( b.dx + c.dx ) + d.dx ) / 6.0
    dvdt = ( a.dv + 2.0 * ( b.dv + c.dv ) + d.dv ) / 6.0

    state.x = state.x + dxdt * dt;
    state.v = state.v + dvdt * dt;



# initial state
state = State(position, velocity)

# numerical integration loop
for x in range( int(duration/timestep) ):
    #
    # could implement a function to vary acceleration here
    #
    rk4(state, acceleration, timestep)


# print results
print('Position: %f m, Velocity: %f m/s after %i second(s)' % (state.x, state.v, duration))
