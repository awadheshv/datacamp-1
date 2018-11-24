'''
Patches

In Bokeh, extended geometrical shapes can be plotted by using the patches() glyph function. The patches glyph takes as input a list-of-lists collection of numeric values specifying the vertices in x and y directions of each distinct patch to plot.

In this exercise, you will plot the state borders of Arizona, Colorado, New Mexico and Utah. The latitude and longitude vertices for each state have been prepared as lists.

Your job is to plot longitude on the x-axis and latitude on the y-axis. The figure object has been created for you as p.
'''

az_lons = [-114.63332, -114.63349, -114.63423, -114.60899, -114.63064, -114.57354, -114.58031, -114.61121,
           -114.67680, -114.66076, -114.65449, -114.68702, -114.69704, -114.70415, -114.67489, -114.70883,
           -114.74365, -114.73513, -114.67290, -114.51122, -114.32346, -114.22646, -114.11390, -114.04404,
           -114.04338, -114.04736, -114.05014, -114.05060, -114.05060, -114.05052, -113.94557, -113.86852,
           -113.62465, -113.47270, -113.32097, -113.17698, -113.02079, -112.99281, -112.96895, -112.75086,
           -112.48455, -112.32985, -111.99142, -111.58602, -111.39598, -111.25230, -111.03957, -110.73783,
           -110.54945, -110.27200, -110.13851, -109.83491, -109.43568, -109.26993, -109.04538, -109.04522,
           -109.04522, -109.04531, -109.04544, -109.04547, -109.04579, -109.04575, -109.04601, -109.04578,
           -109.04606, -109.04621, -109.04636, -109.04662, -109.04644, -109.04598, -109.04603, -109.04633,
           -109.04692, -109.04700, -109.04691, -109.04740, -109.04762, -109.04764, -109.04811, -109.04905,
           -109.04911, -109.05004, -109.05870, -109.25062, -109.30069, -109.33682, -109.38186, -109.45105,
           -109.52870, -109.62562, -109.79302, -109.97582, -110.20503, -110.49327, -110.56918, -110.65415,
           -110.77828, -110.87564, -110.93778, -110.94286, -110.97553, -111.12565, -111.24082, -111.29191,
           -111.32558, -111.35740, -111.38483, -111.44337, -111.47861, -111.49725, -111.53479, -111.56975,
           -111.62412, -111.66000, -111.73365, -111.79498, -111.91820, -111.97172, -111.99115, -112.02937,
           -112.09379, -112.13972, -112.15906, -112.21295, -112.32605, -112.39932, -112.43603, -112.52208,
           -112.57141, -112.63294, -112.67695, -112.72356, -112.75567, -112.80550, -112.83423, -112.87110,
           -112.90863, -113.20884, -113.22790, -113.30314, -113.61086, -113.78489, -113.90756, -113.97121,
           -114.11135, -114.20719, -114.25559, -114.28755, -114.38472, -114.61337, -114.77804, -114.81394,
           -114.81518, -114.80524, -114.81037, -114.81335, -114.80551, -114.80529, -114.79282, -114.79206,
           -114.79555, -114.81362, -114.80894, -114.80404, -114.80093, -114.80804, -114.80891, -114.80192,
           -114.79518, -114.78190, -114.77309, -114.76427, -114.74805, -114.74638, -114.74505, -114.74456,
           -114.74203, -114.74000, -114.73874, -114.73062, -114.72924, -114.72377, -114.71994, -114.71919,
           -114.69096, -114.63501, -114.58576, -114.46563, -114.48131, -114.62973, -114.68157, -114.72123,
           -114.61185, -114.54020, -114.49649, -114.52801, -114.51318, -114.49813, -114.43550, -114.35765,
           -114.26017, -114.14737, -114.29195, -114.38169, -114.44166, -114.48236, -114.56953, -114.63305]

co_lons = [-109.04984, -109.06017, -109.06015, -109.05655, -109.05305, -109.05158, -109.05119, -109.05077,
           -109.05132, -109.05077, -109.05087, -109.05088, -109.05093, -109.05088, -109.05051, -109.04899,
           -109.04907, -109.05008, -109.03134, -108.83854, -108.69960, -108.59802, -108.46524, -108.25764,
           -108.10567, -107.91411, -107.75063, -107.55479, -107.35937, -107.27483, -107.12561, -106.91660,
           -106.59389, -106.32621, -106.06118, -105.82273, -105.60473, -105.46928, -105.27560, -105.07514,
           -104.86787, -104.58704, -104.24506, -104.05350, -104.05325, -104.05153, -103.90732, -103.61529,
           -103.46471, -103.30624, -103.00202, -102.88728, -102.76668, -102.55879, -102.38345, -102.23951,
           -102.12861, -102.05156, -102.05154, -102.05152, -102.05145, -102.05143, -102.05144, -102.05144,
           -102.05150, -102.05150, -102.05152, -102.05131, -102.05145, -102.05176, -102.05176, -102.05174,
           -102.05174, -102.05139, -102.05060, -102.04955, -102.04907, -102.04875, -102.04802, -102.04541,
           -102.04514, -102.04524, -102.04494, -102.04501, -102.04479, -102.04452, -102.04447, -102.04431,
           -102.04456, -102.04402, -102.04286, -102.04166, -102.04179, -102.04178, -102.04192, -102.04196,
           -102.04199, -102.04210, -102.04209, -102.04538, -102.05418, -102.07425, -102.09059, -102.17511,
           -102.19751, -102.24848, -102.26493, -102.29933, -102.34378, -102.35537, -102.40232, -102.49444,
           -102.52468, -102.57091, -102.62547, -102.68337, -102.70590, -102.77324, -102.81507, -102.86545,
           -102.89315, -102.92790, -102.97961, -102.98698, -103.00214, -103.00220, -103.01356, -103.26061,
           -103.53892, -103.92627, -104.17265, -104.49245, -104.76311, -105.15658, -105.50752, -105.65760,
           -105.93761, -106.15386, -106.46540, -106.61906, -106.73137, -106.89142, -107.00562, -107.25094,
           -107.41210, -107.49519, -107.86690, -108.20233, -108.52833, -108.74960, -108.89780, -109.04518,
           -109.04522, -109.04531, -109.04519, -109.04583, -109.04582, -109.04191, -109.04159, -109.04304,
           -109.04232, -109.04980]

nm_lons = [-103.55583, -104.00265, -104.64165, -105.14679, -105.90075, -106.55721, -106.63119, -106.62216,
           -106.63325, -106.61103, -106.54568, -106.52834, -106.52861, -106.53181, -106.55963, -106.56993,
           -106.60042, -106.61408, -106.62967, -106.67613, -106.68194, -106.75050, -106.75874, -106.77057,
           -106.82052, -106.87555, -106.89949, -106.93928, -106.96546, -106.98754, -106.99317, -106.99823,
           -106.99882, -107.00056, -107.12556, -107.27730, -107.29766, -107.30930, -107.32402, -107.35469,
           -107.37629, -107.39716, -107.42244, -107.47074, -107.50261, -107.53069, -107.58350, -107.62497,
           -107.62660, -107.62774, -107.62988, -107.63241, -107.63786, -107.64356, -107.65173, -107.66987,
           -107.70084, -107.70821, -107.75058, -107.78890, -107.84105, -107.86238, -107.87110, -107.88551,
           -107.90473, -107.96400, -108.00059, -108.04400, -108.05664, -108.07876, -108.08267, -108.10520,
           -108.15227, -108.17096, -108.19860, -108.20839, -108.20844, -108.20841, -108.20840, -108.20838,
           -108.20837, -108.20830, -108.20814, -108.20819, -108.20835, -108.20869, -108.20855, -108.20852,
           -108.20849, -108.20839, -108.20848, -108.20854, -108.20857, -108.36757, -108.38904, -108.44606,
           -108.47535, -108.53011, -108.61731, -108.65709, -108.70766, -108.71907, -108.72702, -108.73503,
           -108.73904, -108.75060, -108.75906, -108.82206, -108.86103, -108.88692, -109.00061, -109.05004,
           -109.05004, -109.04911, -109.04905, -109.04811, -109.04764, -109.04762, -109.04740, -109.04691,
           -109.04700, -109.04692, -109.04633, -109.04603, -109.04598, -109.04644, -109.04662, -109.04636,
           -109.04621, -109.04606, -109.04578, -109.04601, -109.04575, -109.04579, -109.04547, -109.04544,
           -109.04531, -109.04522, -109.04522, -109.04518, -108.89780, -108.74960, -108.52833, -108.20233,
           -107.86690, -107.49519, -107.41210, -107.25094, -107.00562, -106.89142, -106.73137, -106.61906,
           -106.46540, -106.15386, -105.93761, -105.65760, -105.50752, -105.15658, -104.76311, -104.49245,
           -104.17265, -103.92627, -103.53892, -103.26061, -103.01356, -103.00220, -103.00220, -103.00232,
           -103.00232, -103.00228, -103.00227, -103.00224, -103.00223, -103.00218, -103.00206, -103.00213,
           -103.00215, -103.00210, -103.00214, -103.00218, -103.00237, -103.00218, -103.00230, -103.00226,
           -103.00223, -103.00226, -103.00230, -103.00233, -103.00233, -103.00228, -103.00228, -103.00245,
           -103.00243, -103.02394, -103.04133, -103.04249, -103.04239, -103.04283, -103.04312, -103.04338,
           -103.04362, -103.04374, -103.04376, -103.04993, -103.05727, -103.06464, -103.06478, -103.53275]

ut_lons = [-114.04392, -114.04391, -114.04375, -114.04195, -114.04061, -114.04055, -114.03980, -114.04172,
           -114.03910, -113.80254, -113.64886, -113.49562, -113.36362, -113.20505, -113.10627, -112.96233,
           -112.83266, -112.78175, -112.68558, -112.58229, -112.45023, -112.26534, -112.19850, -112.10309,
           -111.98965, -111.93040, -111.88098, -111.82932, -111.73177, -111.51913, -111.40870, -111.26009,
           -111.14884, -111.04934, -111.04669, -111.04682, -111.04631, -111.04601, -111.04580, -111.04611,
           -111.04648, -111.04667, -111.04688, -111.04686, -110.94406, -110.86384, -110.70521, -110.55878,
           -110.43401, -110.34177, -110.25071, -110.14713, -110.00040, -109.90645, -109.75044, -109.67348,
           -109.63381, -109.51776, -109.43099, -109.30329, -109.05847, -109.05008, -109.04907, -109.04899,
           -109.05051, -109.05088, -109.05093, -109.05088, -109.05087, -109.05077, -109.05132, -109.05077,
           -109.05119, -109.05158, -109.05305, -109.05655, -109.06015, -109.06017, -109.04984, -109.04980,
           -109.04232, -109.04304, -109.04159, -109.04191, -109.04582, -109.04583, -109.04519, -109.04531,
           -109.04522, -109.04538, -109.26993, -109.43568, -109.83491, -110.13851, -110.27200, -110.54945,
           -110.73783, -111.03957, -111.25230, -111.39598, -111.58602, -111.99142, -112.32985, -112.48455,
           -112.75086, -112.96895, -112.99281, -113.02079, -113.17698, -113.32097, -113.47270, -113.62465,
           -113.86852, -113.94557, -114.05052, -114.05060, -114.05187, -114.05264, -114.05198, -114.04939,
           -114.05013, -114.04997, -114.04992, -114.04916, -114.04833, -114.04885, -114.04841, -114.04779,
           -114.04730, -114.04757, -114.04727, -114.04658, -114.04644, -114.04619, -114.04558]

az_lats = [34.87057, 35.00186, 35.00332, 35.07971, 35.11791, 35.14231, 35.21811, 35.37012, 35.49125,
           35.54170, 35.60517, 35.66942, 35.73579, 35.81412, 35.86436, 35.91670, 35.98542, 36.05493,
           36.11546, 36.15058, 36.10119, 36.01461, 36.09833, 36.21464, 36.37619, 36.60322, 36.81700,
           36.99997, 37.00040, 37.00040, 36.99998, 36.99998, 36.99998, 36.99998, 36.99998, 36.99998,
           37.00022, 37.00017, 37.00012, 37.00048, 37.00094, 37.00105, 37.00097, 37.00166, 37.00147,
           37.00102, 37.00247, 37.00325, 37.00383, 36.99828, 36.99845, 36.99831, 36.99910, 36.99926,
           36.99908, 36.99908, 36.99897, 36.85310, 36.70384, 36.54513, 36.41637, 36.29154, 36.18724,
           36.03128, 35.93088, 35.81044, 35.65092, 35.45859, 35.30697, 34.91388, 34.71264, 34.44558,
           34.08446, 33.71335, 33.34770, 33.07165, 32.70386, 32.40743, 32.17710, 31.87069, 31.63698,
           31.33250, 31.33252, 31.33380, 31.33396, 31.33400, 31.33394, 31.33406, 31.33393, 31.33408,
           31.33399, 31.33341, 31.33363, 31.33296, 31.33299, 31.33305, 31.33363, 31.33328, 31.33281,
           31.33283, 31.33257, 31.34898, 31.38586, 31.40231, 31.41305, 31.42333, 31.43196, 31.45068,
           31.46195, 31.46780, 31.47995, 31.49099, 31.50825, 31.51945, 31.54305, 31.56227, 31.60120,
           31.61823, 31.62425, 31.63623, 31.65645, 31.67094, 31.67701, 31.69377, 31.72891, 31.75165,
           31.76301, 31.78954, 31.80473, 31.82357, 31.83702, 31.85130, 31.86132, 31.87666, 31.88514,
           31.89671, 31.90787, 31.99917, 32.00540, 32.02905, 32.12566, 32.17992, 32.21797, 32.23760,
           32.28088, 32.31044, 32.32538, 32.33509, 32.36468, 32.43408, 32.48373, 32.49526, 32.50602,
           32.50999, 32.51839, 32.52419, 32.53277, 32.54351, 32.55396, 32.56772, 32.56625, 32.56133,
           32.57093, 32.58137, 32.59550, 32.60317, 32.61295, 32.62380, 32.62325, 32.62470, 32.63705,
           32.65006, 32.66489, 32.66985, 32.67414, 32.67850, 32.68221, 32.68517, 32.68732, 32.69860,
           32.70545, 32.71192, 32.71829, 32.71943, 32.73946, 32.73137, 32.73487, 32.87408, 32.97206,
           33.03255, 33.23376, 33.39691, 33.47131, 33.58709, 33.69690, 33.84446, 33.91285, 33.96372,
           34.04257, 34.12866, 34.17212, 34.31087, 34.41527, 34.47903, 34.64288, 34.71453, 34.79181,
           34.86997]

co_lats = [38.21500, 38.40118, 38.60929, 38.81393, 38.95788, 39.11656, 39.22605, 39.36423, 39.56752,
           39.79876, 40.03782, 40.18844, 40.29290, 40.41493, 40.50615, 40.68445, 40.87296, 41.00066,
           41.00051, 41.00013, 41.00010, 40.99996, 41.00008, 41.00011, 41.00139, 41.00205, 41.00197,
           41.00228, 41.00305, 41.00283, 41.00305, 41.00315, 41.00213, 40.99927, 40.99700, 40.99701,
           40.99722, 40.99766, 40.99818, 40.99830, 40.99826, 41.00153, 41.00162, 41.00139, 41.00141,
           41.00153, 41.00166, 41.00170, 41.00185, 41.00191, 41.00239, 41.00231, 41.00234, 41.00243,
           41.00245, 41.00235, 41.00247, 40.97899, 40.92550, 40.87501, 40.82214, 40.75901, 40.71742,
           40.69984, 40.65115, 40.61334, 40.55651, 40.48846, 40.31022, 40.16050, 40.01399, 40.00308,
           40.00061, 39.87098, 39.67645, 39.53889, 39.40853, 39.33572, 39.24305, 38.84279, 38.66387,
           38.59586, 38.52933, 38.47219, 38.41997, 38.30634, 38.26504, 38.17556, 38.05734, 37.94303,
           37.80941, 37.68749, 37.49347, 37.45597, 37.33850, 37.22191, 37.10676, 36.99352, 36.99302,
           36.99306, 36.99305, 36.99311, 36.99325, 36.99357, 36.99367, 36.99420, 36.99439, 36.99425,
           36.99441, 36.99457, 36.99479, 36.99494, 36.99487, 36.99513, 36.99504, 36.99520, 36.99557,
           36.99885, 36.99977, 36.99959, 36.99944, 36.99908, 36.99855, 36.99852, 37.00010, 37.00010,
           37.00021, 36.99956, 36.99892, 36.99669, 36.99511, 36.99367, 36.99350, 36.99527, 36.99589,
           36.99578, 36.99556, 36.99469, 36.99378, 36.99303, 36.99263, 37.00014, 37.00001, 37.00001,
           37.00000, 37.00001, 37.00000, 36.99924, 36.99927, 36.99887, 36.99885, 36.99908, 36.99908,
           37.01706, 37.09597, 37.20443, 37.35363, 37.56670, 37.78990, 37.97469, 38.10272, 38.21472]

nm_lats = [32.00032, 32.00001, 32.00041, 32.00050, 32.00198, 32.00076, 31.98981, 31.93601, 31.90997,
           31.84661, 31.80540, 31.78318, 31.78328, 31.78391, 31.78394, 31.78395, 31.78399, 31.78400,
           31.78409, 31.78395, 31.78393, 31.78371, 31.78394, 31.78404, 31.78385, 31.78384, 31.78379,
           31.78378, 31.78381, 31.78370, 31.78369, 31.78367, 31.78367, 31.78355, 31.78354, 31.78377,
           31.78367, 31.78366, 31.78367, 31.78365, 31.78367, 31.78365, 31.78360, 31.78365, 31.78366,
           31.78365, 31.78369, 31.78365, 31.78374, 31.78374, 31.78374, 31.78374, 31.78370, 31.78371,
           31.78371, 31.78368, 31.78368, 31.78368, 31.78361, 31.78363, 31.78365, 31.78360, 31.78359,
           31.78359, 31.78360, 31.78363, 31.78365, 31.78361, 31.78357, 31.78351, 31.78350, 31.78353,
           31.78357, 31.78358, 31.78359, 31.78360, 31.74465, 31.72969, 31.72323, 31.71940, 31.71733,
           31.68878, 31.62561, 31.58935, 31.56080, 31.52581, 31.50105, 31.49980, 31.47883, 31.42917,
           31.37656, 31.35610, 31.33340, 31.33340, 31.33341, 31.33347, 31.33344, 31.33336, 31.33329,
           31.33323, 31.33319, 31.33307, 31.33298, 31.33290, 31.33285, 31.33273, 31.33261, 31.33226,
           31.33232, 31.33231, 31.33217, 31.33224, 31.33250, 31.63698, 31.87069, 32.17710, 32.40743,
           32.70386, 33.07165, 33.34770, 33.71335, 34.08446, 34.44558, 34.71264, 34.91388, 35.30697,
           35.45859, 35.65092, 35.81044, 35.93088, 36.03128, 36.18724, 36.29154, 36.41637, 36.54513,
           36.70384, 36.85310, 36.99897, 36.99908, 36.99908, 36.99885, 36.99887, 36.99927, 36.99924,
           37.00000, 37.00001, 37.00000, 37.00001, 37.00001, 37.00014, 36.99263, 36.99303, 36.99378,
           36.99469, 36.99556, 36.99578, 36.99589, 36.99527, 36.99350, 36.99367, 36.99511, 36.99669,
           36.99892, 36.99956, 37.00021, 37.00010, 37.00006, 36.96860, 36.95031, 36.91582, 36.91402,
           36.90243, 36.89755, 36.86996, 36.81735, 36.76898, 36.74295, 36.71930, 36.70130, 36.68525,
           36.67653, 36.65329, 36.62780, 36.60265, 36.59190, 36.56927, 36.56386, 36.54875, 36.52963,
           36.51475, 36.50609, 36.50046, 36.50040, 36.50042, 35.76515, 35.21202, 35.13620, 34.88888,
           34.67259, 34.53564, 34.40999, 34.27181, 34.03983, 33.71754, 33.35051, 33.00011, 32.59516,
           32.00034]

ut_lats = [40.68928, 40.68985, 40.76026, 41.05548, 41.36000, 41.59062, 41.89425, 41.99372, 41.99367,
           41.98895, 41.99102, 41.99331, 41.99384, 41.99645, 41.99735, 41.99841, 41.99938, 41.99973,
           42.00021, 42.00054, 42.00099, 42.00111, 42.00116, 41.99763, 41.99834, 41.99861, 41.99856,
           41.99875, 41.99926, 41.99951, 42.00063, 42.00132, 42.00154, 42.00159, 42.00157, 42.00034,
           41.83664, 41.64119, 41.52149, 41.41513, 41.36572, 41.20441, 41.10318, 41.00917, 40.99760,
           40.99725, 40.99635, 40.99635, 40.99485, 40.99533, 40.99609, 40.99634, 40.99734, 40.99766,
           40.99797, 40.99841, 40.99830, 40.99871, 40.99964, 41.00064, 41.00069, 41.00066, 40.87296,
           40.68445, 40.50615, 40.41493, 40.29290, 40.18844, 40.03782, 39.79876, 39.56752, 39.36423,
           39.22605, 39.11656, 38.95788, 38.81393, 38.60929, 38.40118, 38.21500, 38.21472, 38.10272,
           37.97469, 37.78990, 37.56670, 37.35363, 37.20443, 37.09597, 37.01706, 36.99908, 36.99908,
           36.99926, 36.99910, 36.99831, 36.99845, 36.99828, 37.00383, 37.00325, 37.00247, 37.00102,
           37.00147, 37.00166, 37.00097, 37.00105, 37.00094, 37.00048, 37.00012, 37.00017, 37.00022,
           36.99998, 36.99998, 36.99998, 36.99998, 36.99998, 36.99998, 37.00040, 37.00040, 37.13439,
           37.47222, 37.70735, 37.77873, 37.95499, 38.20495, 38.55049, 38.75165, 38.90545, 39.08777,
           39.23851, 39.36296, 39.45715, 39.61018, 39.75817, 39.99994, 40.09896, 40.30302, 40.49580]

from bokeh.plotting import figure
from bokeh.io import output_file, show

p = figure(x_axis_label='longtitude (degrees)', y_axis_label='latitude (degrees)')

'''
INSTRUCTIONS

*   Create a list of the longitude positions for each state as x. This has already been done for you.
*   Create a list of the latitude positions for each state as y. The variable names for the latitude positions are az_lats, co_lats, nm_lats, and ut_lats.
*   Use p.patches() to add the patches glyph to the figure p. Supply the x and y lists as arguments along with a line_color of 'white'.
'''

# Create a list of az_lons, co_lons, nm_lons and ut_lons: x
x = [az_lons, co_lons, nm_lons, ut_lons]

# Create a list of az_lats, co_lats, nm_lats and ut_lats: y
y = [az_lats, co_lats, nm_lats, ut_lats]

# Add patches to figure p with line_color=white for x and y
p.patches(x, y, line_color='white')

# Specify the name of the output file and show the result
output_file('four_corners.html')
show(p)
