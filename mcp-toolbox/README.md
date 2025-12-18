 # Querying BigQuery Datasets using ADK Agents and MCP Toolbox                                                                                                     
                                                                                                                                                                    
   ## Overview                                                                                                                                                       
                                                                                                                                                                      
    This project demonstrates how to build a powerful agent capable of querying BigQuery datasets using the Agent Development Kit (ADK) and the                       
     Model-Context-Protocol (MCP) Toolbox. The agent can understand natural language queries, translate them into SQL, execute them on BigQuery, and return the        
     results.                                                                                                                                                          
                                                                                         u                                                                         
  ## Architecture                                                                                                                                                                                                                                                                                                                 
  The architecture consists of the following components:                                                                                                            
  Understanding their requests, and orchestrating the tools to fulfill them.                                                                                          
  **MCP Toolbox:** A server that exposes a set    of tools to the ADK agent via the Model-Context-Protocol (MCP). These tools provide the agent with the           
   capabilities to interact with BigQuery.                                                                                                                           
  **BigQuery:** Google's serverless, highly scalable data warehouse. The agent will query datasets stored in BigQuery.                                          
                                                                                                                                                                  
  The agent receives a user's query, identifies the intent to query data, and then uses the appropriate tool from the MCP Toolbox to execute a SQL query against    
     BigQuery.                                                                                                                                                         
                                                                                                                                                                   
## Agents and MCP Toolbox for Databases                                                                                                                           
                                                                                                                                                                   
  **ADK Agents:** The Agent Development Kit allows developers to build sophisticated agents that can reason, plan, and use tools to accomplish complex tasks.   
   These agents are not just simple chatbots; they can be configured with specific instructions and have access to a variety of tools to interact with external      
    systems.                                                                                                                                                          
                                                                                                                                                                 
 *   **MCP Toolbox for Databases:** The MCP Toolbox acts as a bridge between the agent and the database. It exposes database operations (like executing SQL        
    queries) as tools that the agent can use. This has several advantages:                                                                                            
     *   **Abstraction:** The agent doesn't need to know the specifics of how to connect to or query the database. It just needs to know how to use the tool.      
      *   **Security:** The MCP Toolbox can enforce security policies, ensuring that the agent only has access to the data it's supposed to.                        
      *   **Modularity:** You can easily add new tools to the toolbox to extend the agent's capabilities.                                                           
                                                                                                                                                                     
   ## Project Structure                                                                                                                                              
                                                                                                                                                                    
                                                                                                                                                               
  __mcp-toolbox                                                                                                                                                              
  ── my-agents/                                                                                                                                                    
     ├── .venv/                                                                                                                                                    
     ├── gcp_releasenotes_agent_app/                                                                                                                               
     │   ├── agent.py                                                                                                                                              
    │   │   └── ...                                                                                                                                                   
     └── ...                                                                                                                                                       
├── toolbox/                                                                                                                                                      
     ├── tools.yaml   
└── README.md                                                                                                                                                     
                                                                                                                                                              
                                                                                                                                                                  
 *   `my-agents/`: Contains the source code for the ADK agents.
 *    *   `my-agents/gcp_releasenotes_agent_app/agent.py`: The main entry point for the agent application.
    `toolbox/`: Contains the implementation of the MCP toolbox server.                                                                                            
      `tools.yaml`: Configuration file for the tools provided by the MCP toolbox.
 *   `README.md`: This file                                                                                                                                                                                                                                                                                                         
 ## Getting Started                                                                                                                                                
                                                                                                                                                                 
 ### Prerequisites                                                                                                                                                 
                                                                                                                                                                  
 *   Python 3.10+                                                                                                                                                  
 *   Google Cloud SDK                                                                                                                                              
 *    Access to a Google Cloud project with the BigQuery API enabled.                                                                                               
                                                                                                                                                                 
### Installation                                                                                                                                                  
                                                                                                                                                                     
  **Clone the repository:**                                                                                                                                     
                                                                                                                                                        
     git clone https://github.com/Madhu-712/Querying-Bigquery-datsets-using-ADK-agents-and-MCP-toolbox.git                                                         
     cd Querying-Bigquery-datsets-using-ADK-agents-and-MCP-toolbox                                                                                                 
                                                                                                                                                         
                                                                                                                                                                   
  **Set up a Python virtual environment:**                                                                                                                      
                                                                                                                                                       
    python3 -m venv .venv                                                                                                                                         
    source .venv/bin/activate                                                                                                                                     
                                                                                                                                                        
                                                                                                                                                                 
.  **Install the dependencies:**                                                                                                                                 
                                                                                                                                                     
    pip install -r my-agents/requirements.txt                                                                                                                     
                                                                                                                                                             
                                                                                                                                                               
  **Authenticate with Google Cloud:**                                                                                                                           
                                                                                                                                                          
     gcloud auth application-default login                                                                                                                         
                                                                                                                                                               
                                                                                                                                                               
## End-to-end Implementation (Steps of Execution)                                                                                                                 
                                                                                                                                                                 
 1.  **Start the MCP Toolbox Server:**                                                                                                                             
     Run the MCP toolbox server to expose the BigQuery tools.                                                                                                      
                                                                                                                                                                  
 2.  **Run the ADK Agent:**                                                                                                                                        
     Execute the main agent script. This will start the conversational agent.                                                                                      
                                                                                                                                                                   
3.  **Interact with the Agent:**                                                                                                                                  
     You can now interact with the agent in your terminal. Ask it questions about your BigQuery data. For example:                                                 
    "Show me the total number of customers in the customers table."                                                                                               
                                                                                                                                                                  
 The agent will then use the tools from the MCP toolbox to execute the corresponding SQL query on BigQuery and return the result to you.                           
                                                                                                                                                                 
 ## Contribution                                                                                                                                                   
                                                                                                                                                                  
    Contributions are welcome! Please feel free to submit a pull request.                                                                                             
                                                                                                                                                                    
 1.  Fork the repository.                                                                                                                                          
 2.  Create a new branch: `git checkout -b my-feature-branch`                                                                                                      
 3.  Make your changes and commit them: `git commit -m 'Add some feature'`                                                                                         
 4.  Push to the branch: `git push origin my-feature-branch`                                                                                                       
                                                                                                                                                                
 ## License                                                                                                                                                        
                                                                                                                                                                  
 This project is licensed under the MIT License. See the `LICENSE` file for details.                                                                               
│                                                                                                                                                                 
 ## Resources                                                                                                                                                      
                                                                                                                                                                   
(https://codelabs.developers.google.com/mcp-toolbox-bigquery-dataset#3)     
