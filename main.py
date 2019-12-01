from database import Database
import json

if __name__ == "__main__":
	with open("Json_Tests/graph_build.json") as json_file:
		build = json.load(json_file)

	if len(build) > 0:
		db = Database(build[0][0])
		if len(build) > 1:
			db.add_nodes(build[1:])

	with open("Json_Tests/img_extract.json") as json_file:
		extract = json.load(json_file)
	db.add_extract(extract)

	with open("Json_Tests/graph_edits.json") as json_file:
		graph_edits = json.load(json_file)
	db.add_nodes(graph_edits)
	
	with open("result_graph.json", 'w') as json_file:
		result = json.dump(db.get_extract_status(), json_file)
	
	with open("result_graph.json") as json_file:
	 	results = json.load(json_file)

	with open("Json_Tests/expected_status.json") as json_file:
	 	expected = json.load(json_file)
	
	# Prints True if the expected and results files contetnts are the same
	print(sorted(expected.items()) == sorted(results.items()))
	#print(db.get_extract_status())
