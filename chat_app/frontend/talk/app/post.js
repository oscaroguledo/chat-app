import { useState } from 'react';
import { Link, Stack } from 'expo-router';
import { Image, SafeAreaView, FlatList, StyleSheet, Text, View, Button} from 'react-native';
import Header from '../components/header/_header';
import {ItemSeparator, Item, PostItem} from "../components/List/List_Item";
import { COLORS,FONT,SIZES } from '../constants/theme';

const persons = [
    {
      id: "1",
      name: "Earnest Green",
    },
    {
      id: "2",
      name: "Winston Orn",
    },
    {
      id: "3",
      name: "Carlton Collins",
    },
    {
      id: "4",
      name: "Malcolm Labadie",
    },
    {
      id: "5",
      name: "Michelle Dare",
    },
    {
      id: "6",
      name: "Carlton Zieme",
    },
    {
      id: "7",
      name: "Jessie Dickinson",
    },
    {
      id: "8",
      name: "Julian Gulgowski",
    },
    {
      id: "9",
      name: "Ellen Veum",
    },
    {
      id: "10",
      name: "Lorena Rice",
    },
  
    {
      id: "11",
      name: "Carlton Zieme",
    },
    {
        id: "12",
        name: "Jessie Dickinson",
      },
      {
        id: "13",
        name: "Julian Gulgowski",
      },
      {
        id: "14",
        name: "Ellen Veum",
      },
      {
        id: "15",
        name: "Lorena Rice",
      },
      {
        id: "16",
        name: "Jessie Dickinson",
      },
      {
        id: "17",
        name: "Julian Gulgowski",
      },
      {
        id: "18",
        name: "Ellen Veum",
      },
      {
        id: "19",
        name: "Lorena Rice",
      },
    {
      id: "20",
      name: "Jessie Dickinson",
    },
    {
      id: "21",
      name: "Julian Gulgowski",
    },
    {
      id: "22",
      name: "Ellen Veum",
    },
    {
      id: "23",
      name: "Lorena Rice",
    },
  ];
function Posts() {
  const [selectedId, setSelectedId] = useState();

  const renderItem = ({item}) => {
      const backgroundColor = item.id === selectedId ? COLORS.selectbackground : COLORS.background;
      const color = item.id === selectedId ? COLORS.selectprimaryText : COLORS.primaryText;
  
      return (
          <View>
              <Item
                  item={item}
                  onPress={() => setSelectedId(item.id)}
                  backgroundColor={backgroundColor}
                  textColor={color}
              />
              <ItemSeparator/>
          </View>
        
      );
    };
    const [postsselectedId, setPostsSelectedId] = useState();

    const renderPostsItem = ({item}) => {
      const backgroundColor = item.id === postsselectedId ? COLORS.selectbackground : COLORS.background;
      const color = item.id === postsselectedId ? COLORS.selectprimaryText : COLORS.primaryText;

      return (
          <View style={{borderRadius: SIZES.xxxLarge / 1.25, backgroundColor:COLORS.primaryColor,padding:SIZES.xxxSmall, margin:SIZES.xSmall}}>
              <PostItem
                    item={item}
                    onPress={() => setpostsSelectedId(item.id)}
                    backgroundColor={backgroundColor}
                    textColor={color}
                    borderRadius={SIZES.xxxLarge / 1.25}
                />
          </View>
        
      );
    };
    const [refreshing, setRefreshing] = useState(false);

    const onRefresh = () => {
      setRefreshing(true);

      // Refresh data here

      setRefreshing(false);
    };

    return (
        <SafeAreaView style={styles.container}>
            <Header title="Posts"></Header>
            <View>
              <Text style={{"fontWeight":FONT.bold,"marginHorizontal":SIZES.xSmall,"marginTop":SIZES.xSmall}}>Contacts</Text>
              <FlatList
                  data={persons}
                  refreshing={refreshing}
                  onRefresh={onRefresh}
                  renderItem={renderPostsItem}
                  keyExtractor={item => item.id}
                  extraData={selectedId}
                  horizontal={true}
                  stickySectionHeadersEnabled={true}
                  showsHorizontalScrollIndicator={false}
                  style={{padding:SIZES.xSmall,backgroundColor:COLORS.background}}
              />
            </View>
            <View>
              <View style={{flexDirection:'row', alignItems:'center',justifyContent: 'space-between'}}>
                <Text style={{"fontWeight":FONT.bold,"marginHorizontal":SIZES.xSmall,"marginBottom":SIZES.xSmall}}>Discover</Text>
                <Text style={{"fontWeight":FONT.bold,"marginHorizontal":SIZES.xSmall,"marginBottom":SIZES.xSmall}}>Instagram</Text>
              </View>
              <FlatList
                data={persons}
                refreshing={refreshing}
                onRefresh={onRefresh}
                renderItem={renderItem}
                keyExtractor={item => item.id}
                extraData={selectedId}
                showsVerticalScrollIndicator={false}
                style={{padding:SIZES.xSmall,backgroundColor:COLORS.background}}
            />
            </View>
            
        </SafeAreaView>
    );
}

export default Posts;

const styles = StyleSheet.create({
    container: {
      flex: 1,
    },
    item: {
      padding: 20,
      fontSize: 15,
      marginTop: 8,
    }
  });