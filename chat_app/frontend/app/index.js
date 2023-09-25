import { useState } from "react";
import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { View, Text, SafeAreaView, ScrollView } from "react-native";
import { Stack, useRouter } from "expo-router";

import {COLORS, icons, images, SIZES} from "../constants";
import {Welcome,Nearbyjobs, Popularjobs, ScreenHeaderBtn} from "../components";
   

function App(){
    const router = useRouter();
    return(
        <SafeAreaView style={{flex:1, backgroundColor:COLORS.lightWhite }}>
            <Stack.Screen 
                options={{
                    headerStyle:{backgroundColor:COLORS.lightWhite},
                    headerShadowVisible:false,
                    headerLeft: () => ( 
                        <ScreenHeaderBtn iconURL={icons.menu} dimension="60%"/>
                    ),
                    headerRight: () => ( 
                        <ScreenHeaderBtn iconURL={images.profile} dimension="100%"/>
                    ),
                    headerTitle:"oscar",
                    headerTitleAlign:"center"
            }}
            />
            
        </SafeAreaView>
    )
}

export default App;