"""
Utopia MODEL
Operation mode
"""

# Import of the Model

from hypatia import Model
import os
from hypatia import Plotter

#%% 
# Create the model using as input the sets files
OptimizationMode = "Single"

Utopia = Model(
    path="examples/Operation_teaching/sets",                           # Path to the sets folder
    mode="Operation",                                                  # "Planning" or "Operation" mode
    optimization = OptimizationMode
)

#%% 
# Create the parameters with default values

# Utopia.create_data_excels(
#     path ='examples\Operation_teaching\parameters',                    # Path to the parameters folder
#     force_rewrite=True                                                 # Overwrite the parameters files (True) or not (False)
# )

#%% 
# Read the parameters

Utopia.read_input_data("examples\Operation_teaching\parameters")       # Path to the parameters folder

#%% 
# Run the model to find the optimal solution
# if OptimizationMode == "Single":
Utopia.run(
    solver='gurobi',                                                  # Selection of the solver: 'GUROBI', 'CVXOPT', 'ECOS', 'ECOS_BB', 'GLPK', 'GLPK_MI', 'OSQP', 'SCIPY', 'SCS’
    verbosity=True,
    force_rewrite= True                                                 # Overwrite the parameters files (True) or not (False)
)
# else:
#     Utopia.run_multi_obj(
#         solver='gurobi',
#         verbosity=True,
#         force_rewrite=True
#     )

#%% 
# Create the folder where to save the results

# os.mkdir("examples/Operation_teaching/results/")                       # Path to the results folder

#%% 
# Save the results as csv file in the previous folder

Utopia.to_csv(
    path='examples/Operation_teaching/results',                         # Path to the destination folder for the results
    force_rewrite=True,                                                 # Overwrite the parameters files (True) or not (False)
    postprocessing_module="aggregated"                                  # "default" and "aggregated" are the two options
)

#%% 
# Create the configuration file for the plots

# Utopia.create_config_file(
#     path = 'examples/Operation_teaching/config.xlsx'                   # Path to the config file
# )

#%% 
# Read the configuration file

plots = Plotter(
    results = Utopia,                                                   # Name of the Model
    config = 'examples/Operation_teaching/config.xlsx',                 # Path to the config file
    hourly_resolution = True,                                           # if model has an hourly resultion otherwise False
)

#%% 
# Create folder for the plots

# os.mkdir("examples/Operation_teaching/plots/") 

#%% 
# Plot the total capacity of each technology in the tech_group in each year and save it in the plots folder 

plots.plot_total_capacity(
    path = 'examples/Operation_teaching/plots/totalcapacity.html',      # Path to the folder in which the plot will be saved
    tech_group = 'Power Generation',                                    # The group of the techs, reported in the configuration file, to be plotted
    kind= "bar",                                                        # "Bar" or "Area" are the two kind of plots accepted
    decom_cap=True,                                                     # Decommissioning capacity can be included (True) or not (False)
    regions="all",                                                      # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=False                                                     # True to aggregate the results of each region, False to plot them separately
)

#%% 
# Plot the annual production of each technology in the tech_group in each year and save it in the plots folder 

plots.plot_prod_by_tech(
    path = 'examples/Operation_teaching/plots/prod_by_tech.html',       # Path to the folder in which the plot will be saved
    tech_group = 'Power Generation',                                    # The group of the techs, reported in the configuration file, to be plotted
    kind="bar",                                                         # "Bar" or "Area" are the two kind of plots accepted
    regions="all",                                                      # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=False                                                     # True to aggregate the results of each region, False to plot them separately
)

#%% 
# Plot the annual consumption of each carrier in the fuel_group in each year and save it in the plots folder 

plots.plot_use_by_technology(
    path = 'examples/Operation_teaching/plots/use_by_tech.html',        # Path to the folder in which the plot will be saved
    fuel_group = 'Natural Gas',                                                 # The group of the carriers, reported in the configuration file, to be plotted
    kind="bar",                                                         # "Bar" or "Area" are the two kind of plots accepted
    regions="all",                                                      # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=False                                                     # True to aggregate the results of each region, False to plot them separately
)

#%%
# Plot as Pie chart the annual consumption and production of each carrier in the fuel_group for a specific year and save it in the plots folder

plots.plot_fuel_prod_cons(
    path = 'examples/Operation_teaching/plots/prod_con_share.html',   # Path to the folder in which the plot will be saved
    years = ["Y0"],                                                     # Year considered 
    fuel_group = 'Electricity',                                         # The group of the carriers, reported in the configuration file, to be plotted
    trade=True,                                                         # Trade can be included (True) or not (False)
    regions="all",                                                      # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=False                                                     # True to aggregate the results of each region, False to plot them separately
)

#%% 
# Plot the annual emission of the emission_type for each technology in the tech_group in each year and save it in the plots folder

plots.plot_emissions(
    path = 'examples/Operation_teaching/plots/emissions.html',          # Path to the folder in which the plot will be saved
    tech_group = 'Power Generation',                                    # The group of the techs, reported in the configuration file, to be plotted
    emission_type = ["CO2 emissions"],                                            # The type of the emissions, reported in the configuration file, to be plotted
    kind="bar",                                                         # "Bar" or "Area" are the two kind of plots accepted
    regions="all",                                                      # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=False                                                      # Global emission can be plotted (True) or emission for each region (False)
)

#%%
# Plot the hourly production of the carrier in the fuel_group for each tech in the tech_group, from the start to the end time

plots.plot_hourly_prod_by_tech(
    path = 'examples/Operation_teaching/plots/hourlyprod_January.html',     # Path to the folder in which the plot will be saved
    tech_group = 'Power Generation',                                        # The group of the techs, reported in the configuration file, to be plotted
    fuel_group = 'Electricity',                                             # The group of the carriers, reported in the configuration file, to be plotted
    kind = "bar",                                                           # "Bar" or "Area" are the two kind of plots accepted
    year = ["Y0"],                                                          # Year considered 
    start="2020-01-01 00:00:00",                                            # Starting day and time ("YYYY-MM-DD hh:mm:ss")
    end="2020-01-01 23:00:00",                                              # Ending day and time ("YYYY-MM-DD hh:mm:ss")
    regions="all",                                                          # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=False                                                         # Global hourly production can be plotted (True) or emission for each region (False)
)

plots.plot_hourly_prod_by_tech(
    path = 'examples/Operation_teaching/plots/hourlyprod_July.html',        # Path to the folder in which the plot will be saved
    tech_group = 'Power Generation',                                        # The group of the techs, reported in the configuration file, to be plotted
    fuel_group = 'Electricity',                                             # The group of the carriers, reported in the configuration file, to be plotted
    kind = "bar",                                                           # "Bar" or "Area" are the two kind of plots accepted
    year = ["Y0"],                                                          # Year considered 
    start="2020-07-01 00:00:00",                                            # Starting day and time ("YYYY-MM-DD hh:mm:ss")
    end="2020-07-01 23:00:00",                                              # Ending day and time ("YYYY-MM-DD hh:mm:ss")
    regions="all",                                                          # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=False                                                         # Global hourly production can be plotted (True) or emission for each region (False)
)

#%%
# Plot the annual costs in each year and save it in the plots folder

plots.plot_regional_costs(
    path = 'examples/Operation_teaching/plots/regionalcosts_bytechs.html',  # Path to the folder in which the plot will be saved
    stacked_by = 'techs',                                                   # Plot can be stacked by "techs" or by cost "items"
    exclude_tech_groups=[],                                                 # Excluded tech groups
    exclude_cost_items=[],                                                  # Excluded cost items
    regions="all",                                                          # The regions considered. "all" to consider all of them, ["reg1", ...] to consider only some regions
    aggregate=False                                                         # Global costs can be plotted (True) or emission for each region (False)
)

