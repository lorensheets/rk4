'''
An implementation of Runge-Kutta 4th order numerical integration, to estimate
position and velocity with respect to time and given acceleration. In this
example, acceleration is constant as only gravity is accounted for, but can
be varied as a function of force and mass.
'''

from vector3d import Vector3D

# initial params
timestep     = 0.01 # [ms]
duration     = 2.0 # [s]

position     = Vector3D([0.0, 9.8, 0.0])
velocity     = Vector3D([0.0, 0.0, 0.0])
acceleration = Vector3D([0.0,-9.8, 0.0])



class State(object):

    def __init__(self, x = 0.0, v = 0.0):
        self.p  = x  # position
        self.v  = v  # velocity



class State3D(object):

    def __init__(self, position, velocity):
        self.vector = [State(p, v) for p, v in zip(position.points, velocity.points)]



class Derivative(object):

    def __init__(self, dp = 0.0, dv = 0.0):
        self.dp = dp    # velocity
        self.dv = dv    # acceleration



def eval(initial, accel, dt, d):

    state = State()
    state.p   = initial.p + d.dp * dt
    state.v   = initial.v + d.dv * dt

    output = Derivative()
    output.dp = state.v
    output.dv = accel

    return output



def rk4(state, dv, dt):
    ''' Implements Runge-Kutta 4th order numerical integration.'''

    a       = eval(state, dv, dt, Derivative())
    b       = eval(state, dv, dt*0.5, a)
    c       = eval(state, dv, dt*0.5, b)
    d       = eval(state, dv, dt, c)

    dpdt    = ( a.dp + 2.0 * ( b.dp + c.dp ) + d.dp ) / 6.0
    dvdt    = ( a.dv + 2.0 * ( b.dv + c.dv ) + d.dv ) / 6.0

    state.p = state.p + dpdt * dt;
    state.v = state.v + dvdt * dt;




state = State3D(position, velocity)

# numerical integration loop
for x in range( int(duration/timestep) ):
    #
    # could implement a function to vary acceleration here
    #
    for s, a in zip(state.vector, acceleration.points):
        rk4(s, a, timestep)



# print results
print('X Position: %r m, X Velocity: %r m/s after %i second(s)' % (state.vector[0].p, state.vector[0].v, duration))
print('Y Position: %r m, Y Velocity: %r m/s after %i second(s)' % (state.vector[1].p, state.vector[1].v, duration))
print('Z Position: %r m, Z Velocity: %r m/s after %i second(s)' % (state.vector[2].p, state.vector[2].v, duration))
