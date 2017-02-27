# AnalysisOfCatan

Summary
An Analysis Of Settlers of Catan vanilla version to try and see the fastest way to gain victory points through simulations.

The settlers of catan rules can be found online: http://www.catan.com/en/download/?SoC_rv_Rules_091907.pdf

The standard vanilla rules will be used when implementing the simulation. All constraints will be applied based on the availbale pieces available to the player. The standard map setting found in the game's manual will be used for the simulation.

Objective:

The objective is to find some sort of an "optimal" path or actions needed by the player to achieve a quick victory. This is done by trying to optimize the fastest accumulation of victory ponts while keeping the lowest amount of turns needed to achieve a total of 10 victory points.

Strategy:

The strategy to find out the optimal path for users is to use an evolving strategy where combination of actions will be added in or taken out in order to help minimize the amount of steps needed to gain 10 victory points. Some analysis will be used at first to help understand and gain an intuition into how fast the user can gain victory points based on certain strategies hardcoded in, or found online.