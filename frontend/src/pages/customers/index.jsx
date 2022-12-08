import React from "react";
import { Box, Button, Typography, Breadcrumbs, useTheme } from "@mui/material";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import { tokens } from "../../theme";
import { useNavigate } from "react-router-dom";
import Header from "../../components/Header";
import { mockDataCustomers } from "../../data/mockData";

const Customers = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const navigate = useNavigate();
  const columns = [
    {
      field: "first_name",
      headerName: "Customer",
      width: 200,
      hieght: 200,
      renderCell: ({ row: { first_name, last_name, avator } }) => {
        return (
          <Box className="flex gap-4 items-center py-2 w-full h-full">
            <img
              className="h-[60px] w-[60px] pointer rounded-[50%]"
              src={avator}
              alt={`${first_name}-${last_name}`}
            />
            <Typography color={colors.grey[100]}>
              {first_name} {last_name}
            </Typography>
          </Box>
        );
      },
    },
    { field: "email", headerName: "Email", width: 200 },
    { field: "orders", headerName: "Orders", width: 100 },

    {
      field: "total_spent",
      headerName: "Total spent",
      width: 100,
      renderCell: ({ row: { total_spent } }) => {
        return <Typography color={colors.greenAccent[500]}>${total_spent}</Typography>;
      },
    },
    { field: "city", headerName: "City", width: 200 },
    
    { field: "last_seen", headerName: "Last seen", width: 100 },
    { field: "last_order", headerName: "Last order", width: 100 },
  ];

  return (
    <Box className="">
      <Box className={`container mx-auto my-[40px]`}>
        <Breadcrumbs aria-label="breadcrumb">
          <Button
            onClick={() => navigate(`/`)}
            variant="text"
            color="secondary"
            className={`bg-opacity-0 hover:bg-opacity-100 px-4 py-2 ${
              "hover:bg-" + colors.greenAccent[400]
            }`}
          >
            Admin Dashboadrd
          </Button>
          <Typography color="text.primary">Customers</Typography>
        </Breadcrumbs>
      </Box>
      <Box className={`container mx-auto py-[20px] my-4 flex flex-col gap-4`}>
        <Box display="flex" justifyContent="space-between" alignItems="center">
          <Header title="Customers" subtitle="welcome to you Customers" />
        </Box>
        <Box className="flex gap-4">
          <Box className="flex gap-1">
            <Typography>All</Typography>
            <Typography color={colors.greenAccent[500]}>(10000)</Typography>
          </Box>
          <Box className="flex gap-1">
            <Typography>Publishd</Typography>
            <Typography color={colors.greenAccent[500]}>(5600)</Typography>
          </Box>
          <Box className="flex gap-1">
            <Typography>All</Typography>
            <Typography color={colors.greenAccent[500]}>(540)</Typography>
          </Box>
          <Box className="flex gap-1">
            <Typography>On Discount</Typography>
            <Typography color={colors.greenAccent[500]}>(800)</Typography>
          </Box>
        </Box>
        <Box
          className="h-[80vh]"
          height="80vh"
          sx={{
            "& .MuiDataGrid-root": {
              border: "none",
            },
            "& .MuiDataGrid-cell": {
              borderBottom: "none",
            },
            "& .name-column--cell": {
              color: colors.greenAccent[300],
            },
            "& .MuiDataGrid-columnHeaders": {
              backgroundColor: colors.blueAccent[700],
              borderBottom: "none",
            },
            "& .MuiDataGrid-virtualScroller": {
              backgroundColor: colors.primary[400],
            },
            "& .MuiDataGrid-footerContainer": {
              borderTop: "none",
              backgroundColor: colors.blueAccent[700],
            },
            "& .MuiCheckbox-root": {
              color: `${colors.greenAccent[200]} !important`,
            },
            "& .MuiChackbox-root": {
              color: `${colors.greenAccent[200]} !important`,
            },
          }}
        >
          <DataGrid
            density="comfortable"
            rows={mockDataCustomers}
            columns={columns}
            autoPageSize
            checkboxSelection
            components={{ Toolbar: GridToolbar }}
          />
        </Box>
      </Box>
    </Box>
  );
};

export default Customers;
