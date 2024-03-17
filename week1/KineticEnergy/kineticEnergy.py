def kinetic_energy(mass, velocity):
    kineticE = 0.5 * (mass) * (pow(velocity, 2))
    return kineticE
def main():
    mass = float(input('Enter values for mass: '))
    velocity = float(input('Enter values for velocity: '))
    ke = kinetic_energy(mass, velocity)
    print(f'The kinetic energy of {mass} kg and {velocity} m/s: {ke}')
main()