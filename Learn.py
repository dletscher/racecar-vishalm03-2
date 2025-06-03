import sys, importlib, argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description ='Simulate the Mountain Car.')
	parser.add_argument('agent_file')
	parser.add_argument('data_file')
	parser.add_argument('num_steps', type=int)
	args = parser.parse_args()

	try:
		agentModule = importlib.import_module(args.agent_file.split('.')[0])
	except:
		print('Invalid agent module')
		sys.exit()
		
	agent = agentModule.Agent()
	try:
		agent.load(args.data_file)
	except:
		print('Could not load data, starting with zeros')

	agent.train(args.num_steps)
	
	agent.save(args.data_file)
