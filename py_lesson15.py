## Simple function with one positional argument/parameter
def prettify_string(input_str):
    """ Attempts to prettify input string parameters
    Parameters:
    input_str (str): the function input which should be string

    Returns:
    str: Returns the trimmed and titled string
   """
    output_str = input_str.strip().title()  # the task to be run
    return output_str


## function multiple positional argument
def convert_pressure(value, from_unit, to_unit):
    """ Convert pressure from field unit to si unit and vice versa
    Parameters:
        value (float): input pressure numeric value
        from_unit (str): input unit for pressure
        to_unit (str): desired output unit for pressure
    Returns:
        float: Returns the converted pressure value
   """
    CONVERSION_FACTOR = 0.145038  # it is a convention to use capital letter for naming constant value
    if from_unit.lower() == 'kpa' and to_unit.lower() == 'psia':
        output_value = value * CONVERSION_FACTOR
    elif from_unit.lower() == 'psia' and to_unit.lower() == 'kpa':
        output_value = value / CONVERSION_FACTOR
    else:
        output_value = 'This operation is not supported yet!'

    return output_value


## function with default parameter
def calc_bottom_hole_pressure(well_length, fluid_density=1000.0):
    return well_length * 9.81 * fluid_density


## function with arbitrary number of arguments
def calc_simple_average(*args):
    summation = 0.0
    for arg in args:
        summation += arg

    # another approach would be
    # return sum(args)/len(args)

    return summation / len(args)


def get_sw_from_archie(rt, rw, *args, **kwargs):
    '''
    use Archie Method to calculate water saturation
    sw=((a / phi ** m) * (rw / rt)) ** (1.0 / n))
    :param rt (float>0):  true resistivity of the formation, corrected for invasion, borehole, thin bed, and other effects
    :param rw (float>0):  formation water resistivity at formation temperature
    :param args (float *porosity):  value(s) of porosity for which sw is desired
    :param kwargs {n:2, m:2.0, a:1}: dictionary containing the saturation exponent, cementation exponent, tortuosity exponent (unitless)
    :return float: water saturation(s)
    '''

    a = 1.0
    n = 2.0  # default value for n
    m = 2.0  # default value for m
    if kwargs.get('n'):  # one way of checking if user has provided parameter (n) in kwargs
        n = kwargs['n']
    if 'm' in kwargs:  # second way of checking if user has provided parameter (m) in kwargs
        m = kwargs['m']
    if kwargs.get('a'):
        a = kwargs.get('a')

    sws = []
    for arg in args:
        sws.append(((a / arg ** m) * (rw / rt)) ** (1.0 / n))

    return sws


## Function use or call (prettify string)
reservoir_names = ['nisKu', '  Wabamun', ' CardIum']
# how to use function
# for name in reservoir_names:
#     prettified_name = prettify_string(name)  # this is where we call the function
#     print(prettified_name)

## Call convert pressure function
pressure_values = [(1230, 'kpa', 'psia'),
                   (1345.7, 'psia', 'kpa'),
                   (34, 'MPa', 'kPa')]
# for p_value in pressure_values:
#     print(f"{convert_pressure(p_value[0], p_value[1], p_value[2])}")

## use the BHP calculator function
## use without providing the second argument
# print(f"BHP for 1000m long well is {calc_bottom_hole_pressure(1000) * 1e-6:0.1f} MPa.")
## use with providing the second argument
# print(f"BHP for 1000m long well is {calc_bottom_hole_pressure(1000, 750) * 1e-6:0.1f} MPa.")

## use function with *arg parameters
# print(calc_simple_average(0.1056, 0.2045, 0.5689))

poro_values = [0.1056, 0.2045, 0.5689]
## wrong way of calling the calc_avg_pressure function
## will throw error
# print(calc_simple_average(poro_values))
# print(calc_simple_average(*poro_values))  # enforce to treat input parameters as iterable


porosities = [0.33, 0.265, 0.22]
kwargs = {'m': 2.15, 'a': 0.62}
sw_values = get_sw_from_archie(20, 0.9, *porosities, **kwargs)
print(f" @Phi={porosities}-->Sw={sw_values}")
