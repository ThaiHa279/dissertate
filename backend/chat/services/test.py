from sentence_transformers import SentenceTransformer, util
sentences = ["Cô giáo đang ăn kem", "Chị gái đang thử món thịt dê"]

model = SentenceTransformer('keepitreal/vietnamese-sbert')
embeddings = model.encode(sentences)
# Compute cosine-similarities
cosine_scores = util.cos_sim(embeddings[0], embeddings[1])


print(cosine_scores)
