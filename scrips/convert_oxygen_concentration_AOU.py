def convert_oxygen_concentration(oxygen_in_mg_per_L, salinity, temperature, pressure):
    """
    Convert oxygen concentration from mg/L to micromol/kg in seawater.

    Parameters:
    oxygen_in_mg_per_L (float): Oxygen concentration in mg/L
    salinity (float): Absolute Salinity in g/kg
    temperature (float): Conservative Temperature in degrees Celsius
    pressure (float): Sea pressure in dbar

    Returns:
    float: Oxygen concentration in micromol/kg
    """
    import gsw

    # Molecular weight of O2
    molecular_weight_O2 = 31.9988  # g/mol

    # Convert mg/L to mol/L
    oxygen_in_mol_per_L = oxygen_in_mg_per_L / (1000 * molecular_weight_O2)

    # Convert mol/L to micromol/L
    oxygen_in_micromol_per_L = oxygen_in_mol_per_L * 1e6

    # Calculate density of seawater in kg/L
    density_seawater = gsw.rho(salinity, temperature, pressure) / 1000  # kg/L

    # Convert micromol/L to micromol/kg
    oxygen_in_micromol_per_kg = oxygen_in_micromol_per_L / density_seawater

    return oxygen_in_micromol_per_kg


def calculate_aou(salinity, temperature, pressure, oxygen, latitude, longitude):
    """
    Calculate Apparent Oxygen Utilization (AOU).

    Parameters:
    salinity (float): Absolute Salinity in g/kg; 
    Practical Salinity Unit (PSU) is a unit based on the properties of seawater conductivity. 
    It's a dimensionless unit, but it's roughly equivalent to or grams per kilogram (g/kg)
    temperature (float): Conservative Temperature in degrees Celsius
    pressure (float): Sea pressure in dbar
    oxygen (float): Dissolved oxygen concentration in micromol/kg

    Returns:
    float: AOU in micromol/kg
    Reference:

    TEOS-10 Manual
    GSW-Python Documentation
    """
    import gsw

    # Calculate saturation concentration of oxygen in micromol/kg
    oxygen_sat = gsw.O2sol(salinity, temperature, pressure, latitude, longitude)

    # Calculate AOU
    aou = oxygen_sat - oxygen

    return aou
