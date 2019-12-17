import util
model = util.restore_model('../models/developmental/best_model_architecture.json', '../models/developmental/best_model_weights.h5')
import satimage
satimage.generate_predictions(model, '../images', '../data/predicted_developmental.csv')
