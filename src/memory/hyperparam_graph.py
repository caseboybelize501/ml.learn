from neo4j import GraphDatabase
from typing import Dict, Any

class HyperparamGraph:
    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        
    def close(self):
        self.driver.close()
    
    def add_hyperparam_relationship(self, hyperparam: str, eval_stage: str,
                                  hardware_config: str, relationship_type: str):
        # Add relationship between hyperparam and evaluation stage
        with self.driver.session() as session:
            session.write_transaction(
                self._create_relationship,
                hyperparam=hyperparam,
                eval_stage=eval_stage,
                hardware_config=hardware_config,
                relationship_type=relationship_type
            )
    
    @staticmethod
    def _create_relationship(tx, hyperparam: str, eval_stage: str,
                          hardware_config: str, relationship_type: str):
        query = """
        MERGE (h:Hyperparam {name: $hyperparam})
        MERGE (e:EvalStage {name: $eval_stage})
        MERGE (hw:Hardware {config: $hardware_config})
        MERGE (h)-[:%s]->(e)
        MERGE (h)-[:%s]->(hw)
        """ % (relationship_type, relationship_type)
        
        tx.run(query, hyperparam=hyperparam, eval_stage=eval_stage,
               hardware_config=hardware_config)