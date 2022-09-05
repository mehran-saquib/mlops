import pickle

reg_model=pickle.load(open('reg_model.pickle','rb'))


def predict(property_type,room_type,accommodates,bathrooms,bed_type,cancellation_policy,cleaning_fee,city,instant_bookable,bedrooms,beds):
    
    property_encoded=[0 for i in range(0,35)]

    match property_type:
        case "Apartment":
            property_encoded[0]=1
        case  "House":
            property_encoded[1]=1
        case  "Condominium":
            property_encoded[2]=1
        case  "Loft":
            property_encoded[3]=1
        case  "Townhouse":
            property_encoded[4]=1
        case  "Hostel":
            property_encoded[5]=1
        case  "Guest suite":
            property_encoded[6]=1
        case  "Bed & Breakfast":
            property_encoded[7]=1
        case  "Bungalow":
            property_encoded[8]=1
        case  "Guesthouse":
            property_encoded[9]=1
        case  "Dorm":
            property_encoded[10]=1
        case "Other":
            property_encoded[11]=1
        case  "Camper/RV":
            property_encoded[12]=1
        case  "Villa":
            property_encoded[13]=1
        case  "Boutique hotel":
            property_encoded[14]=1
        case  "Timeshare":
            property_encoded[15]=1
        case  "In-law":
            property_encoded[16]=1
        case  "Boat":
            property_encoded[17]=1
        case  "Serviced apartment":
            property_encoded[18]=1
        case  "Castle":
            property_encoded[19]=1
        case  "Cabin":
            property_encoded[20]=1
        case  "Treehouse":
            property_encoded[21]=1
        case  "Tipi":
            property_encoded[22]=1
        case  "Vacation home":
            property_encoded[23]=1
        case "Tent":
            property_encoded[24]=1
        case  "Hut":
            property_encoded[25]=1
        case  "Casa particular":
            property_encoded[26]=1
        case  "Chalet":
            property_encoded[27]=1
        case  "Yurt":
            property_encoded[28]=1
        case  "Earth House":
            property_encoded[29]=1
        case  "Parking Space":
            property_encoded[30]=1
        case  "Train":
            property_encoded[31]=1
        case  "Cave":
            property_encoded[32]=1
        case  "Lighthouse":
            property_encoded[33]=1
        case  "Island":
            property_encoded[34]=1
    
    room_type_encoded=[0,0,0]

    match room_type:
        case "Entire home/apt":
            room_type_encoded[0]=1
        case  "Private room":
            room_type_encoded[1]=1
        case  "Shared room":
            room_type_encoded[2]=1
    
    bed_type_encoded=[0,0,0,0,0]

    match bed_type:
        case "Real Bed":
            bed_type_encoded[0]=1
        case  "Futon":
            bed_type_encoded[1]=1
        case  "Pull-out Sofa":
            bed_type_encoded[2]=1
        case  "Couch":
            bed_type_encoded[3]=1
        case  "Airbed":
            bed_type_encoded[4]=1
    
    cancellation_encoded=[0,0,0,0,0]

    match cancellation_policy:
        case "strict":
            cancellation_encoded[0]=1
        case  "moderate":
            cancellation_encoded[1]=1
        case  "flexible":
            cancellation_encoded[2]=1
        case  "super_strict_30":
            cancellation_encoded[3]=1
        case  "super_strict_60":
            cancellation_encoded[4]=1

    cleaning_fee_encoded=[0,0]

    match cleaning_fee:
        case "True":
            cleaning_fee_encoded[0]=1
        case  "False":
            cleaning_fee_encoded[1]=1
    
    city_encoded=[0,0,0,0,0,0]

    match city:
        case "NYC":
            city_encoded[0]=1
        case  "SF":
            city_encoded[1]=1
        case  "DC":
            city_encoded[2]=1
        case  "LA":
            city_encoded[3]=1
        case  "Chicago":
            city_encoded[4]=1
        case  "Boston":
            city_encoded[5]=1
    
    instant_bookable_encoded=[0,0]

    match instant_bookable:
        case "t":
            instant_bookable_encoded[0]=1
        case  "f":
            instant_bookable_encoded[1]=1
    
    input_data=[accommodates,bathrooms,bedrooms,beds]+property_encoded+room_type_encoded+bed_type_encoded+cancellation_encoded+cleaning_fee_encoded+city_encoded+instant_bookable_encoded

    a=reg_model.predict([input_data])
    return a[0]