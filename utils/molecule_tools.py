
def lipinski_flags(row):
    """Simple Lipinski-style rule flags from common descriptor columns."""
    flags = []
    if row.get("MW", 0) > 500:
        flags.append("MW > 500")
    if row.get("LogP", 0) > 5:
        flags.append("LogP > 5")
    if row.get("HBD", 0) > 5:
        flags.append("HBD > 5")
    if row.get("HBA", 0) > 10:
        flags.append("HBA > 10")
    return flags or ["No major Lipinski flag"]
