//     const getNowDate = () => {
//     const today = new Date();
//     return today.toLocaleDateString("en-US");
//   };
import { constants } from "./constants";
export const initialValues = {
  title: "",
  description: "",
  price: 0,
  brand: "",
  thumbnail: [],
  images: [],
  category: "",
  collection: "",
  vendor: "",
  tags: "",
  variants: constants.variants,
  restockQuantity: 0,
  globalDelivery: {
    type: "",
    selectedCountries: [],
  },
  attributes: {
    fragileProduct: false,
    biodegradable: false,
    frozenProduct: {
      selected: false,
      maxAllowedTemperature: "",
    },
    expiryDate: {
      selected: false,
      date: "",
    },
  },
  advanced: {
    productIDType: "",
    productID: "",
  },
};