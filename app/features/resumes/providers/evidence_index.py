"""Synthetic resume evidence indexing with stable passage IDs; STEP-3.
ICS provider; component be.evidence_index.
"""
import re

def index_evidence(document_id:str,text:str)->list[dict[str,str]]:
    """Split paragraphs into directly cited evidence records."""
    if not document_id:raise ValueError("document id required")
    return [{"id":f"{document_id}:{i}","text":p.strip()} for i,p in enumerate(text.split("\n")) if p.strip()]

def retrieve_evidence(passages:list[dict[str,str]],query:str)->list[dict[str,str]]:
    """Deterministic lexical evidence retrieval; no inferred applicant claims."""
    terms=set(re.findall(r"[a-z]+",query.lower()))
    ranked=sorted(passages,key=lambda p:len(terms.intersection(set(re.findall(r"[a-z]+",p["text"].lower())))),reverse=True)
    return [p for p in ranked if terms.intersection(set(re.findall(r"[a-z]+",p["text"].lower())))][:5]
