import numpy as np
from matplotlib import colors

whitedarkjet_arr = \
    np.array(
        [[1.0000000, 1.0000000, 1.0000000],
         [0.9843100, 0.9882400, 0.9960800],
         [0.9686300, 0.9803900, 0.9882400],
         [0.9529400, 0.9686300, 0.9803900],
         [0.9372500, 0.9568600, 0.9725500],
         [0.9215700, 0.9451000, 0.9647100],
         [0.9058800, 0.9372500, 0.9607800],
         [0.8902000, 0.9254900, 0.9529400],
         [0.8745100, 0.9137300, 0.9451000],
         [0.8588200, 0.9058800, 0.9372500],
         [0.8431400, 0.8941200, 0.9294100],
         [0.8274500, 0.8823500, 0.9215700],
         [0.8117600, 0.8705900, 0.9137300],
         [0.7960800, 0.8627500, 0.9058800],
         [0.7803900, 0.8509800, 0.8980400],
         [0.7647100, 0.8392200, 0.8941200],
         [0.7490200, 0.8313700, 0.8862700],
         [0.7333300, 0.8196100, 0.8784300],
         [0.7176500, 0.8078400, 0.8705900],
         [0.7019600, 0.7960800, 0.8627500],
         [0.6862700, 0.7882400, 0.8549000],
         [0.6705900, 0.7764700, 0.8470600],
         [0.6549000, 0.7647100, 0.8392200],
         [0.6392200, 0.7568600, 0.8352900],
         [0.6235300, 0.7451000, 0.8274500],
         [0.6078400, 0.7333300, 0.8196100],
         [0.5921600, 0.7215700, 0.8117600],
         [0.5764700, 0.7137300, 0.8039200],
         [0.5607800, 0.7019600, 0.7960800],
         [0.5451000, 0.6902000, 0.7882400],
         [0.5294100, 0.6823500, 0.7803900],
         [0.5137300, 0.6705900, 0.7764700],
         [0.4980400, 0.6588200, 0.7686300],
         [0.4823500, 0.6470600, 0.7607800],
         [0.4666700, 0.6392200, 0.7529400],
         [0.4509800, 0.6274500, 0.7451000],
         [0.4352900, 0.6156900, 0.7372500],
         [0.4196100, 0.6078400, 0.7294100],
         [0.4039200, 0.5960800, 0.7215700],
         [0.3882400, 0.5843100, 0.7176500],
         [0.3725500, 0.5725500, 0.7098000],
         [0.3568600, 0.5647100, 0.7019600],
         [0.3411800, 0.5529400, 0.6941200],
         [0.3254900, 0.5411800, 0.6862700],
         [0.3098000, 0.5333300, 0.6784300],
         [0.2941200, 0.5215700, 0.6705900],
         [0.2784300, 0.5098000, 0.6627500],
         [0.2627500, 0.4980400, 0.6549000],
         [0.2470600, 0.4902000, 0.6509800],
         [0.2313700, 0.4784300, 0.6431400],
         [0.2156900, 0.4666700, 0.6352900],
         [0.2000000, 0.4588200, 0.6274500],
         [0.1843100, 0.4470600, 0.6196100],
         [0.1686300, 0.4352900, 0.6117600],
         [0.1529400, 0.4235300, 0.6039200],
         [0.1372500, 0.4156900, 0.5960800],
         [0.1215700, 0.4039200, 0.5921600],
         [0.1058800, 0.3921600, 0.5843100],
         [0.0901960, 0.3843100, 0.5764700],
         [0.0745100, 0.3725500, 0.5686300],
         [0.0588240, 0.3607800, 0.5607800],
         [0.0431370, 0.3490200, 0.5529400],
         [0.0274510, 0.3411800, 0.5451000],
         [0.0117650, 0.3294100, 0.5372500],
         [0.0000000, 0.3215700, 0.5333300],
         [0.0078431, 0.3294100, 0.5254900],
         [0.0117650, 0.3372500, 0.5176500],
         [0.0156860, 0.3451000, 0.5137300],
         [0.0235290, 0.3529400, 0.5058800],
         [0.0274510, 0.3607800, 0.4980400],
         [0.0352940, 0.3686300, 0.4941200],
         [0.0392160, 0.3764700, 0.4862700],
         [0.0431370, 0.3843100, 0.4784300],
         [0.0509800, 0.3921600, 0.4745100],
         [0.0549020, 0.4000000, 0.4666700],
         [0.0588240, 0.4078400, 0.4588200],
         [0.0666670, 0.4156900, 0.4549000],
         [0.0705880, 0.4196100, 0.4470600],
         [0.0784310, 0.4274500, 0.4392200],
         [0.0823530, 0.4352900, 0.4352900],
         [0.0862750, 0.4431400, 0.4274500],
         [0.0941180, 0.4509800, 0.4196100],
         [0.0980390, 0.4588200, 0.4156900],
         [0.1019600, 0.4666700, 0.4078400],
         [0.1098000, 0.4745100, 0.4000000],
         [0.1137300, 0.4823500, 0.3960800],
         [0.1176500, 0.4902000, 0.3882400],
         [0.1254900, 0.4980400, 0.3803900],
         [0.1294100, 0.5058800, 0.3764700],
         [0.1372500, 0.5137300, 0.3686300],
         [0.1411800, 0.5215700, 0.3607800],
         [0.1451000, 0.5254900, 0.3568600],
         [0.1529400, 0.5333300, 0.3490200],
         [0.1568600, 0.5411800, 0.3411800],
         [0.1607800, 0.5490200, 0.3372500],
         [0.1686300, 0.5568600, 0.3294100],
         [0.1725500, 0.5647100, 0.3215700],
         [0.1803900, 0.5725500, 0.3176500],
         [0.1843100, 0.5803900, 0.3098000],
         [0.1882400, 0.5882400, 0.3019600],
         [0.1960800, 0.5960800, 0.2980400],
         [0.2000000, 0.6039200, 0.2902000],
         [0.2039200, 0.6117600, 0.2823500],
         [0.2117600, 0.6196100, 0.2784300],
         [0.2156900, 0.6235300, 0.2705900],
         [0.2235300, 0.6313700, 0.2666700],
         [0.2274500, 0.6392200, 0.2588200],
         [0.2313700, 0.6470600, 0.2509800],
         [0.2392200, 0.6549000, 0.2470600],
         [0.2431400, 0.6627500, 0.2392200],
         [0.2470600, 0.6705900, 0.2313700],
         [0.2549000, 0.6784300, 0.2274500],
         [0.2588200, 0.6862700, 0.2196100],
         [0.2627500, 0.6941200, 0.2117600],
         [0.2705900, 0.7019600, 0.2078400],
         [0.2745100, 0.7098000, 0.2000000],
         [0.2823500, 0.7176500, 0.1921600],
         [0.2862700, 0.7254900, 0.1882400],
         [0.2902000, 0.7294100, 0.1803900],
         [0.2980400, 0.7372500, 0.1725500],
         [0.3019600, 0.7451000, 0.1686300],
         [0.3058800, 0.7529400, 0.1607800],
         [0.3137300, 0.7607800, 0.1529400],
         [0.3176500, 0.7686300, 0.1490200],
         [0.3254900, 0.7764700, 0.1411800],
         [0.3294100, 0.7843100, 0.1333300],
         [0.3333300, 0.7921600, 0.1294100],
         [0.3411800, 0.8000000, 0.1215700],
         [0.3490200, 0.8039200, 0.1176500],
         [0.3568600, 0.8039200, 0.1137300],
         [0.3686300, 0.8078400, 0.1137300],
         [0.3803900, 0.8078400, 0.1098000],
         [0.3882400, 0.8117600, 0.1098000],
         [0.4000000, 0.8117600, 0.1098000],
         [0.4078400, 0.8117600, 0.1058800],
         [0.4196100, 0.8156900, 0.1058800],
         [0.4313700, 0.8156900, 0.1019600],
         [0.4392200, 0.8196100, 0.1019600],
         [0.4509800, 0.8196100, 0.0980390],
         [0.4627500, 0.8235300, 0.0980390],
         [0.4705900, 0.8235300, 0.0941180],
         [0.4823500, 0.8235300, 0.0941180],
         [0.4941200, 0.8274500, 0.0901960],
         [0.5019600, 0.8274500, 0.0901960],
         [0.5137300, 0.8313700, 0.0862750],
         [0.5254900, 0.8313700, 0.0862750],
         [0.5333300, 0.8313700, 0.0823530],
         [0.5451000, 0.8352900, 0.0823530],
         [0.5529400, 0.8352900, 0.0784310],
         [0.5647100, 0.8392200, 0.0784310],
         [0.5764700, 0.8392200, 0.0784310],
         [0.5843100, 0.8392200, 0.0745100],
         [0.5960800, 0.8431400, 0.0745100],
         [0.6078400, 0.8431400, 0.0705880],
         [0.6156900, 0.8470600, 0.0705880],
         [0.6274500, 0.8470600, 0.0666670],
         [0.6392200, 0.8509800, 0.0666670],
         [0.6470600, 0.8509800, 0.0627450],
         [0.6588200, 0.8509800, 0.0627450],
         [0.6705900, 0.8549000, 0.0588240],
         [0.6784300, 0.8549000, 0.0588240],
         [0.6902000, 0.8588200, 0.0549020],
         [0.6980400, 0.8588200, 0.0549020],
         [0.7098000, 0.8588200, 0.0509800],
         [0.7215700, 0.8627500, 0.0509800],
         [0.7294100, 0.8627500, 0.0470590],
         [0.7411800, 0.8666700, 0.0470590],
         [0.7529400, 0.8666700, 0.0431370],
         [0.7607800, 0.8666700, 0.0431370],
         [0.7725500, 0.8705900, 0.0431370],
         [0.7843100, 0.8705900, 0.0392160],
         [0.7921600, 0.8745100, 0.0392160],
         [0.8039200, 0.8745100, 0.0352940],
         [0.8156900, 0.8784300, 0.0352940],
         [0.8235300, 0.8784300, 0.0313730],
         [0.8352900, 0.8784300, 0.0313730],
         [0.8431400, 0.8823500, 0.0274510],
         [0.8549000, 0.8823500, 0.0274510],
         [0.8666700, 0.8862700, 0.0235290],
         [0.8745100, 0.8862700, 0.0235290],
         [0.8862700, 0.8862700, 0.0196080],
         [0.8980400, 0.8902000, 0.0196080],
         [0.9058800, 0.8902000, 0.0156860],
         [0.9176500, 0.8941200, 0.0156860],
         [0.9294100, 0.8941200, 0.0117650],
         [0.9372500, 0.8941200, 0.0117650],
         [0.9490200, 0.8980400, 0.0078431],
         [0.9607800, 0.8980400, 0.0078431],
         [0.9686300, 0.9019600, 0.0078431],
         [0.9803900, 0.9019600, 0.0039216],
         [0.9882400, 0.9058800, 0.0039216],
         [1.0000000, 0.9058800, 0.0000000],
         [1.0000000, 0.8980400, 0.0000000],
         [1.0000000, 0.8862700, 0.0000000],
         [1.0000000, 0.8745100, 0.0000000],
         [1.0000000, 0.8627500, 0.0000000],
         [1.0000000, 0.8509800, 0.0000000],
         [1.0000000, 0.8431400, 0.0000000],
         [1.0000000, 0.8313700, 0.0000000],
         [1.0000000, 0.8196100, 0.0000000],
         [1.0000000, 0.8078400, 0.0000000],
         [1.0000000, 0.7960800, 0.0000000],
         [1.0000000, 0.7843100, 0.0000000],
         [1.0000000, 0.7725500, 0.0000000],
         [1.0000000, 0.7607800, 0.0000000],
         [1.0000000, 0.7529400, 0.0000000],
         [1.0000000, 0.7411800, 0.0000000],
         [1.0000000, 0.7294100, 0.0000000],
         [1.0000000, 0.7176500, 0.0000000],
         [1.0000000, 0.7058800, 0.0000000],
         [1.0000000, 0.6941200, 0.0000000],
         [1.0000000, 0.6823500, 0.0000000],
         [1.0000000, 0.6705900, 0.0000000],
         [1.0000000, 0.6627500, 0.0000000],
         [1.0000000, 0.6509800, 0.0000000],
         [1.0000000, 0.6392200, 0.0000000],
         [1.0000000, 0.6274500, 0.0000000],
         [1.0000000, 0.6156900, 0.0000000],
         [1.0000000, 0.6039200, 0.0000000],
         [1.0000000, 0.5921600, 0.0000000],
         [1.0000000, 0.5803900, 0.0000000],
         [1.0000000, 0.5725500, 0.0000000],
         [1.0000000, 0.5607800, 0.0000000],
         [1.0000000, 0.5490200, 0.0000000],
         [1.0000000, 0.5372500, 0.0000000],
         [1.0000000, 0.5254900, 0.0000000],
         [1.0000000, 0.5137300, 0.0000000],
         [1.0000000, 0.5019600, 0.0000000],
         [1.0000000, 0.4902000, 0.0000000],
         [1.0000000, 0.4823500, 0.0000000],
         [1.0000000, 0.4705900, 0.0000000],
         [1.0000000, 0.4588200, 0.0000000],
         [1.0000000, 0.4470600, 0.0000000],
         [1.0000000, 0.4352900, 0.0039216],
         [1.0000000, 0.4235300, 0.0039216],
         [1.0000000, 0.4117600, 0.0039216],
         [1.0000000, 0.4000000, 0.0039216],
         [1.0000000, 0.3921600, 0.0039216],
         [1.0000000, 0.3803900, 0.0039216],
         [1.0000000, 0.3686300, 0.0039216],
         [1.0000000, 0.3568600, 0.0039216],
         [1.0000000, 0.3451000, 0.0039216],
         [1.0000000, 0.3333300, 0.0039216],
         [1.0000000, 0.3215700, 0.0039216],
         [1.0000000, 0.3137300, 0.0039216],
         [1.0000000, 0.3019600, 0.0039216],
         [1.0000000, 0.2902000, 0.0039216],
         [1.0000000, 0.2784300, 0.0039216],
         [1.0000000, 0.2666700, 0.0039216],
         [1.0000000, 0.2549000, 0.0039216],
         [1.0000000, 0.2431400, 0.0039216],
         [1.0000000, 0.2313700, 0.0039216],
         [1.0000000, 0.2235300, 0.0039216],
         [1.0000000, 0.2117600, 0.0039216],
         [1.0000000, 0.2000000, 0.0039216],
         [1.0000000, 0.1882400, 0.0039216]])

whitedarkjet = colors.ListedColormap(whitedarkjet_arr)
whitedarkjet.set_over(color='black')
whitedarkjet.set_under(color='lime')
