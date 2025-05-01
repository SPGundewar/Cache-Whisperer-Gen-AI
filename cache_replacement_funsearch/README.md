**Gen AI - Cache Replacement Policies using Funsearch**

This project explores generating optimized cache replacement policies using Funsearch.


Setup Instructions:

1. Clone and Build ChampSim

  Clone and build the ChampSim repository parallel to this project directory.

2. Create Traces Folder

  Inside the cache_replacement_funsearch folder, create a folder named traces.

3. Add Traces

  Download and add the trace files you want to test into the traces folder.

4. Set the API key

  In the cache_replacement_funsearch/funsearch_cache_optimizer.py file:
  set GROQ_API_KEY = "#YOUR_API_KEY" 

    pip install groq

5. Run the Optimizer

  Execute the funsearch_cache_optimizer.py script from the root folder to generate and evaluate new cache replacement policies.

    python cache_replacement_funsearch/funsearch_cache_optimizer.py


6. View Generated Policies

  Successfully generated policies will be saved inside the cache_policies folder.


Project Structure:

-cache_replacement_funsearch

├── cache_policies/         # Folder where optimized policies will be stored

├── traces/                 # Folder containing trace files

├── funsearch_cache_optimizer.py   # Main script to run the optimizer

-(ChampSim repository)   # Should be parallel to the cache_replacement_funsearch folder


Notes:
  Ensure all dependencies required by Funsearch and ChampSim are installed.

  Proper trace files are needed for evaluation; example traces can typically be found through HPC folder.
