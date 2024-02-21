from data_structures.hashtable import Hashtable


def left_join(hash1, hash2, join='left'):
    """Left join two hash tables."""
    
    combined = []
    
    if not hash1 or not hash2:
        return []
    
    if not isinstance(hash1, dict) or not isinstance(hash2, dict):
        raise TypeError
    
    if join == 'left':
        primary, secondary = hash1, hash2
    elif join == 'right':
        primary, secondary = hash2, hash1
    else:
        raise ValueError
        
    for key, value in primary.items():
        if key in secondary:
            combined.append([key, value, secondary[key]])
        else:
            combined.append([key, value, "NONE"])
    
    return combined
    
# def left_join(hash1, hash2, optional=0):
#     """Left join two hash tables."""
    
#     combined = []
    
#     if not hash1 or not hash2:
#         return []
    
#     if not isinstance(hash1, dict) or not isinstance(hash2, dict):
#         raise TypeError
    
#     for key, value in hash1.items():
#         if key in hash2:
#             combined.append([key, value, hash2[key]])
#         else:
#             combined.append([key, value, "NONE"])
    
#     return combined

