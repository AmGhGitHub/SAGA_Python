class Well:
    """
    Well class for modelling vertical well
    performance
    """

    def __init__(self, radius, length):
        """
        Initialize well attributes
        :param radius (float): radius of the well
        in ft
        :param length (float): productive length
        of the well in ft
        """
        self.radius = radius
        self.length = length

    def get_wellbore_volume(self, correction_factor=1.0):
        """
        :param correction_factor (float): a correction-factor
        to be applied to volume
        :return (float): storage volume of the
        well is returned
        """
        PI = 3.1415  # by convention, we use all CAPITAL LETTERS name for constant value in Python
        well_volume = PI * self.radius ** 2.0 * self.length * correction_factor
        return well_volume

# create an instance of the class or create an well object
oil_well = Well(0.30, 551)  # please note that init() method requires 3 parameters, but we only provide two parameters
water_well = Well(0.25, 1001.4)

## objects are working independently from each other
print(oil_well.radius > water_well.radius)  # you see the application of "dot" notation with objects
print(f"Internal volume:{oil_well.get_wellbore_volume(0.9):.2f} ft3")


## use the object method
oil_well_internal_vol = oil_well.get_wellbore_volume(0.95)  # again, we don't need to pass any value for the self parameter
water_well_internal_vol = water_well.get_wellbore_volume(0.81)
print(f"Oil-well internal volume:{oil_well_internal_vol}")
print(f"Water-well internal volume:{water_well_internal_vol:.2f}")
